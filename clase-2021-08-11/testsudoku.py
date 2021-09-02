import unittest

from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def test_init(self):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertTrue(type(sudoku_obj.initial_board), list)
        self.assertTrue(type(sudoku_obj.user_board), list)
        self.assertEqual(len(sudoku_obj.initial_board), 9)
        self.assertEqual(len(sudoku_obj.user_board), 9)
        for col in range(9):
            self.assertEqual(len(sudoku_obj.initial_board[col]), 9)
            self.assertEqual(len(sudoku_obj.user_board[col]), 9)

#   validar que el value este entre 1-9

    def test_validate_numbers_OK(self):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertTrue(sudoku_obj.validate_numbers(2, 3, 5))

    def test_validate_numbers_row(self):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertFalse(sudoku_obj.validate_numbers(0, 5, 5))
        self.assertFalse(sudoku_obj.validate_numbers(10, 5, 5))

    def test_validate_numbers_col(self):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertFalse(sudoku_obj.validate_numbers(5, 0, 5))
        self.assertFalse(sudoku_obj.validate_numbers(5, 10, 5))

    def test_validate_numbers_value(self):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertFalse(sudoku_obj.validate_numbers(5, 5, 0))
        self.assertFalse(sudoku_obj.validate_numbers(5, 5, 10))

#   ---------------------------------------------------

    def test_verify_number_is_not_initials_OK(self):
        sudoku_obj = Sudoku()
        # En este caso (fila,columna) el usuario puede modificar porque hay un 0
        sudoku_obj.initial_board[3][2] = 0
        self.assertTrue(sudoku_obj.validate_initial(3, 2))

    def test_verify_number_is_initials_ERROR(self):
        sudoku_obj = Sudoku()
        # En este caso (fila,columna) el usuario NO puede modificar porque 9 es
        # uno de los numeros aleatorios del tablero inicial
        sudoku_obj.initial_board[3][2] = 9
        self.assertFalse(sudoku_obj.validate_initial(3, 2))

    def test_validate_set_value_ok(self):
        sudoku_obj = Sudoku()
        sudoku_obj.set_value(1, 1, 9)
        self.assertEqual(sudoku_obj.user_board[0][0], 9)

    def test_validate_set_value_error_initial_board(self):
        sudoku_obj = Sudoku()
        sudoku_obj.initial_board[0][0] = 5
        sudoku_obj.set_value(1, 1, 9)
        self.assertEqual(sudoku_obj.initial_board[0][0], 5)
        self.assertEqual(sudoku_obj.user_board[0][0], 0)

    def test_validate_row_ok(self):
        sudoku_obj = Sudoku()
        self.assertTrue(sudoku_obj.validate_row(1, 9))

    def test_validate_row_error_initial_board(self):
        sudoku_obj = Sudoku()
        sudoku_obj.initial_board[0][2] = 9
        self.assertFalse(sudoku_obj.validate_row(1, 9))

    def test_validate_row_error_user_board(self):
        sudoku_obj = Sudoku()
        sudoku_obj.user_board[0][2] = 9
        self.assertFalse(sudoku_obj.validate_row(1, 9))


if __name__ == '__main__':
    unittest.main()