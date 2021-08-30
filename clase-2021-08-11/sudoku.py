class Sudoku():
    def __init__(self):
        self.initial_board = []
        for y in range(9):
            self.initial_board.append([0 for x in range(9)])
        self.user_board = [[0 for x in range(9)] for y in range(9)]  # con los numeros que va poniendo el usuario

    def verify_initial(self, row, col):
        return self.initial_board[row][col] == 0


