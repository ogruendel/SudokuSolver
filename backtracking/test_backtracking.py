import unittest
import backtracking


class TestBacktracking(unittest.TestCase):
    def test_check_legal_in_row(self):
        board_1 = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2, 1],
            [1, 0, 0, 2, 3, 0, 6, 5, 8],
            [0, 0, 6, 4, 0, 0, 1, 3, 9],
            [4, 3, 0, 0, 0, 0, 5, 7, 8],
            [0, 0, 1, 1, 4, 5, 6, 7, 8],
            [4, 5, 6, 8, 0, 0, 4, 1, 0],
            [0, 0, 4, 6, 7, 8, 9, 1, 1],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        r = backtracking.check_legal_in_row(board_1, 0, 0)
        self.assertEqual(r, True)
        r = backtracking.check_legal_in_row(board_1, 1, 5)
        self.assertEqual(r, True)
        r = backtracking.check_legal_in_row(board_1, 2, 1)
        self.assertEqual(r, False)
        r = backtracking.check_legal_in_row(board_1, 6, 6)
        self.assertEqual(r, False)

    def test_check_legal_in_col(self):
        board_1 = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 1, 3, 6, 7, 8, 9, 0],
            [4, 1, 2, 0, 4, 0, 0, 5, 7],
            [1, 3, 0, 0, 2, 1, 4, 6, 0],
            [2, 6, 4, 1, 5, 0, 0, 0, 5],
            [3, 4, 0, 2, 9, 8, 5, 1, 2],
            [5, 0, 0, 5, 0, 2, 1, 4, 1],
            [6, 0, 4, 5, 5, 9, 0, 6, 7],
            [7, 4, 5, 8, 8, 0, 0, 0, 0],
        ]
        r = backtracking.check_legal_in_col(board_1, 0, 0)
        self.assertEqual(r, False)
        r = backtracking.check_legal_in_col(board_1, 4, 8)
        self.assertEqual(r, True)
        r = backtracking.check_legal_in_col(board_1, 1, 5)
        self.assertEqual(r, True)
        r = backtracking.check_legal_in_col(board_1, 2, 5)
        self.assertEqual(r, False)