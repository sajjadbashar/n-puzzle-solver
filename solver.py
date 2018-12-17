from search import Search
from state import State

class Solver:
    def __init__(self, board):
        self.board = board
        self.solution = None
        self.states_set = set()
        self.iter_count = 0

    def solve(self, method=Search.BFS):
        self.states_set.clear()
        self.solution = None
        start = time()
        if method == Search.BFS:
            self.bfs(self.board.initial_state)
        elif method == Search.DFS:
            self.dfs(self.board.initial_state, MAX_DEPTH)
        elif method == Search.DFSID:
            self.dfsid()
        elif method == Search.AStar:
            self.a_star(self.board.initial_state)
        end = time()
        print("Elapsed time: %f" % (end - start))
        self.display_result()

    def bfs(self, state):
        queue = deque()
        queue.append(state)
        self.states_set.add(state.to_sequence())
        while queue:
            self.iter_count = self.iter_count + 1
            state = queue.popleft()
            if self.board.is_goal_state(state):
                self.solution = state
                break

            n_state = state.move(Moves.N)
            if n_state is not None:
                sequence = n_state.to_sequence()
                if sequence not in self.states_set:
                    self.states_set.add(sequence)
                    queue.append(n_state)

            e_state = state.move(Moves.E)
            if e_state is not None:
                sequence = e_state.to_sequence()
                if sequence not in self.states_set:
                    self.states_set.add(sequence)
                    queue.append(e_state)

            s_state = state.move(Moves.S)
            if s_state is not None:
                sequence = s_state.to_sequence()
                if sequence not in self.states_set:
                    self.states_set.add(sequence)
                    queue.append(s_state)

            w_state = state.move(Moves.W)
            if w_state is not None:
                sequence = w_state.to_sequence()
                if sequence not in self.states_set:
                    self.states_set.add(sequence)
                    queue.append(w_state)

    def dfs(self, state, depth):
        if depth < 0:
            return
        if self.board.is_goal_state(state):
            self.solution = state
        if self.solution is not None:
            return

        n_state = state.move(Moves.N)
        if n_state is not None:
            sequence = n_state.to_sequence()
            if sequence not in self.states_set:
                self.states_set.add(sequence)
                self.dfs(n_state, depth - 1)
                if self.solution is not None:
                    return

        e_state = state.move(Moves.E)
        if e_state is not None:
            sequence = e_state.to_sequence()
            if sequence not in self.states_set:
                self.states_set.add(sequence)
                self.dfs(e_state, depth - 1)
                if self.solution is not None:
                    return
        s_state = state.move(Moves.S)
        if s_state is not None:
            sequence = s_state.to_sequence()
            if sequence not in self.states_set:
                self.states_set.add(sequence)
                self.dfs(s_state, depth - 1)
                if self.solution is not None:
                    return

        w_state = state.move(Moves.W)
        if w_state is not None:
            sequence = w_state.to_sequence()
            if sequence not in self.states_set:
                self.states_set.add(sequence)
                self.dfs(w_state, depth - 1)
                if self.solution is not None:
                    return

    def dfsid(self, max_depth=MAX_DEPTH):
        for i in range(1, max_depth):
            self.states_set.clear()
            self.dfs(self.board.initial_state, i)
            if self.solution is not None:
                break

    def a_star(self, state):
        open_q = PriorityQueue()
        open_q.put(state)

        while not open_q.empty():
            parent = open_q.get()
            if self.board.is_goal_state(parent):
                self.solution = parent
                return
            children = parent.get_children()
            for child in children:
                if child.to_sequence() not in self.states_set:
                    h_cost = self._manhattan_distance(child)
                    child.score = child.level + h_cost
                    open_q.put(child)
            self.states_set.add(parent.to_sequence())

    def _manhattan_distance(self, state):
        dist = 0
        blank = state.size**2
        for j, row in enumerate(state.state):
            for i, val in enumerate(row):
                if val != blank: dist += abs( (val - 1)%state.size - i ) + abs( (val - 1)//state.size - j)
        return dist

    def display_result(self):
        if self.solution is None:
            print("No solution found!") #Should not happen
            return
        path = []
        last = self.solution
        while last.parent is not None:
            prev = last.parent
            prev = last.parent
            last_i, last_j = last.get_blank_position()
            prev_i, prev_j = prev.get_blank_position()
            dif_i = prev_i - last_i
            dif_j = prev_j - last_j
            path.append(Moves(dif_i * 1 + dif_j * -2))
            last = prev
        path = path[::-1]
        print( " ".join( [ val.name for val in path] ))
