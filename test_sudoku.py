import unittest
import sudoku


class TestSudoku(unittest.TestCase):
    def test_fill_last_num_in_row(self):
        board_1 = [
            [2, 5, 4, 6, 3, 8, 7, 9, 0],
            [9, 1, 3, 0, 7, 2, 8, 6, 5],
            [6, 0, 7, 9, 5, 1, 2, 4, 3],
            [0, 7, 9, 0, 0, 0, 5, 8, 0],
            [1, 6, 2, 0, 0, 9, 4, 0, 7],
            [5, 3, 8, 7, 4, 6, 9, 0, 2],
            [7, 2, 6, 3, 0, 4, 1, 5, 8],
            [3, 0, 0, 8, 0, 0, 6, 0, 9],
            [0, 9, 1, 0, 0, 0, 0, 0, 0]
        ]

        r = sudoku.fill_last_num_in_row(board_1)
        self.assertEqual(r, [
            [2, 5, 4, 6, 3, 8, 7, 9, 1],
            [9, 1, 3, 4, 7, 2, 8, 6, 5],
            [6, 8, 7, 9, 5, 1, 2, 4, 3],
            [0, 7, 9, 0, 0, 0, 5, 8, 0],
            [1, 6, 2, 0, 0, 9, 4, 0, 7],
            [5, 3, 8, 7, 4, 6, 9, 1, 2],
            [7, 2, 6, 3, 9, 4, 1, 5, 8],
            [3, 0, 0, 8, 0, 0, 6, 0, 9],
            [0, 9, 1, 0, 0, 0, 0, 0, 0]
        ])

    def test_fill_last_num_in_col(self):
        board_1 = [
            [8, 1, 7, 9, 0, 0, 3, 4, 5],
            [3, 0, 4, 8, 5, 1, 7, 2, 6],
            [2, 6, 5, 0, 7, 3, 8, 9, 1],
            [4, 7, 2, 5, 6, 8, 9, 0, 0],
            [9, 5, 1, 3, 4, 2, 6, 8, 7],
            [6, 3, 0, 1, 9, 7, 2, 5, 4],
            [0, 4, 6, 2, 1, 9, 0, 3, 8],
            [1, 2, 3, 6, 8, 5, 4, 7, 9],
            [5, 8, 9, 7, 3, 4, 1, 6, 2]
        ]
        r = sudoku.fill_last_num_in_col(board_1)
        self.assertEqual(r, [
            [8, 1, 7, 9, 2, 6, 3, 4, 5],
            [3, 9, 4, 8, 5, 1, 7, 2, 6],
            [2, 6, 5, 4, 7, 3, 8, 9, 1],
            [4, 7, 2, 5, 6, 8, 9, 1, 3],
            [9, 5, 1, 3, 4, 2, 6, 8, 7],
            [6, 3, 8, 1, 9, 7, 2, 5, 4],
            [7, 4, 6, 2, 1, 9, 5, 3, 8],
            [1, 2, 3, 6, 8, 5, 4, 7, 9],
            [5, 8, 9, 7, 3, 4, 1, 6, 2]
        ])

    def test_fill_last_num_in_block(self):
        board_1 = [
            [7, 6, 3, 1, 8, 5, 4, 2, 9],
            [0, 1, 5, 9, 6, 2, 3, 7, 8],
            [9, 2, 8, 3, 0, 4, 0, 6, 1],
            [6, 7, 2, 5, 3, 1, 9, 8, 4],
            [8, 3, 0, 6, 4, 9, 2, 5, 7],
            [5, 4, 9, 0, 2, 7, 6, 1, 0],
            [3, 9, 6, 2, 1, 8, 7, 4, 5],
            [1, 5, 7, 4, 9, 0, 8, 3, 2],
            [0, 8, 4, 7, 5, 3, 1, 0, 6]
        ]

        r = sudoku.fill_last_num_in_block(board_1)
        self.assertEqual(r, [
            [7, 6, 3, 1, 8, 5, 4, 2, 9],
            [4, 1, 5, 9, 6, 2, 3, 7, 8],
            [9, 2, 8, 3, 7, 4, 5, 6, 1],
            [6, 7, 2, 5, 3, 1, 9, 8, 4],
            [8, 3, 1, 6, 4, 9, 2, 5, 7],
            [5, 4, 9, 8, 2, 7, 6, 1, 3],
            [3, 9, 6, 2, 1, 8, 7, 4, 5],
            [1, 5, 7, 4, 9, 6, 8, 3, 2],
            [2, 8, 4, 7, 5, 3, 1, 9, 6]
        ])

    def test_is_solved(self):
        board_1 = [
            [2, 5, 4, 6, 3, 8, 7, 9, 0],
            [9, 1, 3, 0, 7, 2, 8, 6, 5],
            [6, 0, 7, 9, 5, 1, 2, 4, 3],
            [0, 7, 9, 0, 0, 0, 5, 8, 0],
            [1, 6, 2, 0, 0, 9, 4, 0, 7],
            [5, 3, 8, 7, 4, 6, 9, 0, 2],
            [7, 2, 6, 3, 0, 4, 1, 5, 8],
            [3, 0, 0, 8, 0, 0, 6, 0, 9],
            [0, 9, 1, 0, 0, 0, 0, 0, 0]
        ]
        r = sudoku.is_solved(board_1)
        self.assertEqual(r, False)

        board_2 = [
            [7, 6, 3, 1, 8, 5, 4, 2, 9],
            [0, 1, 5, 9, 6, 2, 3, 7, 8],
            [9, 2, 8, 3, 0, 4, 0, 6, 1],
            [6, 7, 2, 5, 3, 1, 9, 8, 4],
            [8, 3, 0, 6, 4, 9, 2, 5, 7],
            [5, 4, 9, 0, 2, 7, 6, 1, 0],
            [3, 9, 6, 2, 1, 8, 7, 4, 5],
            [1, 5, 7, 4, 9, 0, 8, 3, 2],
            [0, 8, 4, 7, 5, 3, 1, 0, 6]
        ]
        r = sudoku.is_solved(board_2)
        self.assertEqual(r, False)

        board_3 = [
            [7, 6, 3, 1, 8, 5, 4, 2, 9],
            [4, 1, 5, 9, 6, 2, 3, 7, 8],
            [9, 2, 8, 3, 7, 4, 5, 6, 1],
            [6, 7, 2, 5, 3, 1, 9, 8, 4],
            [8, 3, 1, 6, 4, 9, 2, 5, 7],
            [5, 4, 9, 8, 2, 7, 6, 1, 3],
            [3, 9, 6, 2, 1, 8, 7, 4, 5],
            [1, 5, 7, 4, 9, 6, 8, 3, 2],
            [2, 8, 4, 7, 5, 3, 1, 9, 6]
        ]
        r = sudoku.is_solved(board_3)
        self.assertEqual(r, True)




