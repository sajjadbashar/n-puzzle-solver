import random
from moves import Moves

class State(object):
    def __init__(self, state, parent=None):
        self.state = [ [x for x in line] for line in state]
        self.size = len(self.state)
        self.score = 0
        self.level = 0
        self.parent = parent

    def get_allowed_moves(self):
        blank_i, blank_j = self.get_blank_position()
        moves = []
        if blank_i > 0 : moves.append(Moves.N)
        if blank_j < self.size - 1 : moves.append(Moves.E)
        if blank_i < self.size - 1 : moves.append(Moves.S)
        if blank_j > 0 : moves.append(Moves.W)

        if self.parent is not None:
            parent = self.parent
            parent_i, parent_j = parent.get_blank_position()
            dif_i = blank_i - parent_i
            dif_j = blank_j - parent_j
            if dif_i > 0 and Moves.N in moves: moves.remove(Moves.N)
            if dif_j > 0 and Moves.E in moves: moves.remove(Moves.E)
            if dif_i < 0 and Moves.S in moves: moves.remove(Moves.S)
            if dif_j < 0 and Moves.W in moves: moves.remove(Moves.W)

        return moves

    def get_blank_position(self):
        for i, line in enumerate(self.state):
            for j, val in enumerate(line):
                if val == 16:
                    return i, j

    def move(self, direction):
        allowed_moves = self.get_allowed_moves()
        if direction not in allowed_moves:
            return None
        state = State(self.state, parent=self)
        state._move(direction)
        return state

    def get_children(self):
        states = []
        allowed_moves = self.get_allowed_moves()
        for move in allowed_moves:
            child = self.move(move)
            child.level += 1
            states.append(child)
        return states

    def randomize(self, steps=15):
        backward = None
        while steps > 0:
            moves = self.get_allowed_moves()
            if backward is not None:
                moves.remove(Moves(backward.value * -1))
            self._move(random.choice(moves))
            steps = steps - 1

    def _move(self, direction):
        i, j = self.get_blank_position()
        if direction == Moves.N:
            self[i][j], self[i-1][j] = self[i-1][j], self[i][j]
        elif direction == Moves.E:
            self[i][j], self[i][j+1] = self[i][j+1], self[i][j]
        elif direction == Moves.S:
            self[i][j], self[i+1][j] = self[i+1][j], self[i][j]
        elif direction == Moves.W:
            self[i][j], self[i][j-1] = self[i][j-1], self[i][j]

    def to_sequence(self):
        return " ".join( [ " ".join([str(val) for val in line]) for line in self.state ] )

    def __gt__(self, other):
        return self.score > other.score

    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def __getitem__(self, index):
        return self.state[index]

    def __str__(self):
        lines = []
        for line in self.state:
            lines.append(" ----"*self.size)
            vals = "|" + "|".join([str(x).center(4) for x in line]) + "|"
            lines.append(vals)
        lines.append(" ----"*self.size)
        return "\n".join(lines)
