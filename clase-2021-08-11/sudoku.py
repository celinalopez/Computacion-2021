class Sudoku():
    def __init__(self):
        self.initial_board = [[0 for x in range(9)] for y in range(9)]  # con los numeros random
        self.user_board = [[0 for x in range(9)] for y in range(9)]  # con los numeros que va poniendo el usuario

    def set_value(self, row, col, value):
        if (
                self.validate_numbers(row, col, value) and
                self.validate_initial(row, col) and
                self.validate_rules(row, col, value)
        ):
            self.user_board[row - 1][col - 1] = value

    def validate_numbers(self, row, col, value):
        return (
                1 <= row <= 9 and
                1 <= col <= 9 and
                1 <= value <= 9
        )

    def validate_initial(self, row, col):  # Valida si es una posicion inicial libre
        return self.initial_board[row - 1][col - 1] == 0

    def validate_rules(self, row, col, value):
        return (
                self.validate_row(row, value) and
                self.validate_col(row, col) and
                self.validate_region(row, col, value)
        )

    def validate_row(self, row, value):
        for col in range(9):
            if (
                    self.initial_board[row - 1][col] == value or
                    self.user_board[row - 1][col] == value
            ):
                return False
        return True

    def validate_col(self, col, value):
        for row in range(9):
            if (
                    self.initial_board[row][col - 1] == value or
                    self.user_board[row][col - 1] == value
            ):
                return False
        return True

    def validate_region(self, row, col, value):
        return True

    def fin_juego(self, row, col):
        suma_row = 0
        suma_col = 0
        for row in range(9):
            suma_col += self.user_board[row][col - 1]
        for col in range(9):
            suma_row = self.user_board[row - 1][col]
        if (
                suma_row and suma_col == 45
        ):
            print("Fin!!!")


def program():
    game = Sudoku()  # esto crea un objeto de la clase...
    while True:
        # le pedimos al usuario que nos diga que jugar...
        col = input('coordenada col (1 a 9)')
        row = input('coordenada fila (1 a 9)')
        value = input('numero (1 a 9)')

        # con esos parametros del usuario tengo que:
        # pero primero validate que los numeros sean de 1 a 9...
        # validar que se cumplan las reglas del juego
        # y poner el numero
        # game. ????? (row, col, value)
        # if game.validate_numbers(row, col, value) and game.validate_rules(row, col, value):
        #     game.set_value(row, col, value)
        game.set_value(row, col, value)
