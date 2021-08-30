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

    def test_verify_number_is_not_initials_OK(self):
        sudoku_obj = Sudoku()
        # quiero probar que en fila, cola no era un valor initial del juego
        sudoku_obj.initial_board[3][2] = 0
        self.assertTrue(sudoku_obj.verify_initial(3, 2))

    def test_verify_number_is_initials_ERROR(self):
        sudoku_obj = Sudoku()
        # quiero probar que en fila, cola si era un valor initial del juego
        sudoku_obj.initial_board[3][2] = 9
        self.assertFalse(sudoku_obj.verify_initial(3, 2))


if __name__ == '__main__':
    unittest.main()