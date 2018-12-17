class Board:
    def __init__(self, size=4):
        self.size = size
        self.name = "".join([str(size*size - 1), "-puzzle" ])
        self.initial_state = None
        self.goal_state = State( [ [i+1 for i in range(j, j + self.size)] for j in range(0, self.size**2, self.size) ] )
        self.init_board()

    def init_board(self):
        def is_solvable(sequence):
            if len(sequence) < 1:
                return False
            return True
        options = range(1, self.size**2 + 1)
        sequence = []
        while not is_solvable(sequence):
            # sequence = random.sample(options, self.size**2)
            sequence = SOLVABLE_15 # for testing
#        initial_state = [ [sequence[i] for i in range(j, j+self.size) ] for j in range(0, self.size**2, self.size)]
        initial_state = [ row[:] for row in self.goal_state ]
        self.initial_state = State(initial_state)
        self.initial_state.randomize(15)

    def is_goal_state(self, state):
        return self.goal_state.to_sequence() == state.to_sequence()

    def __str__(self):
        return str(self.initial_state)
