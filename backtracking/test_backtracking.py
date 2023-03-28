import unittest
import backtracking as b


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

        board_2 = [
            [1, 0, 4, 0, 2, 0, 0, 0, 0],
            [0, 3, 0, 0, 0, 9, 0, 7, 1],
            [0, 9, 6, 0, 0, 0, 4, 0, 5],
            [5, 0, 1, 0, 6, 0, 0, 0, 0],
            [7, 0, 8, 9, 1, 2, 3, 0, 4],
            [3, 0, 9, 4, 0, 5, 6, 1, 8],
            [0, 1, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 3, 7, 0, 4, 0, 0, 0],
            [0, 0, 0, 2, 3, 0, 0, 4, 6]
        ]

        r = b.check_legal_in_row(board_1, 0, 1)
        self.assertEqual(r, False)
        r = b.check_legal_in_row(board_1, 1, 4)
        self.assertEqual(r, False)
        r = b.check_legal_in_row(board_1, 2, 4)
        self.assertEqual(r, True)
        r = b.check_legal_in_row(board_1, 6, 9)
        self.assertEqual(r, True)
        r = b.check_legal_in_row(board_2, 0, 2)
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

        r = b.check_legal_in_col(board_1, 0, 1)
        self.assertEqual(r, False)
        r = b.check_legal_in_col(board_1, 4, 1)
        self.assertEqual(r, True)
        r = b.check_legal_in_col(board_1, 1, 5)
        self.assertEqual(r, True)
        r = b.check_legal_in_col(board_1, 2, 4)
        self.assertEqual(r, False)

    def test_check_legal_in_box(self):
        board_1 = [
            [0, 0, 7, 0, 0, 0, 4, 0, 0],
            [0, 0, 0, 3, 7, 0, 9, 0, 8],
            [0, 9, 0, 0, 0, 5, 7, 6, 0],
            [0, 0, 1, 8, 0, 0, 5, 0, 0],
            [2, 7, 5, 6, 4, 0, 8, 0, 0],
            [9, 4, 8, 5, 3, 0, 6, 7, 2],
            [0, 0, 3, 0, 9, 0, 0, 0, 0],
            [0, 5, 4, 2, 0, 0, 0, 9, 6],
            [1, 0, 9, 7, 0, 3, 0, 0, 0]
        ]

        r = b.check_legal_in_box(board_1, 2, 1, 4)
        self.assertEqual(r, True)
        r = b.check_legal_in_box(board_1, 8, 4, 1)
        self.assertEqual(r, True)
        r = b.check_legal_in_box(board_1, 3, 3, 6)
        self.assertEqual(r, False)
        r = b.check_legal_in_box(board_1, 8, 0, 6)
        self.assertEqual(r, False)

    def test_check_legal(self):
        board_1 = [
            [0, 3, 0, 8, 7, 2, 5, 4, 9],
            [2, 7, 5, 6, 9, 4, 8, 3, 1],
            [9, 4, 8, 0, 1, 3, 6, 7, 0],
            [8, 2, 3, 4, 6, 9, 1, 5, 7],
            [7, 5, 4, 2, 8, 1, 3, 9, 6],
            [1, 6, 9, 7, 3, 5, 2, 8, 4],
            [3, 8, 7, 9, 2, 6, 4, 1, 5],
            [4, 9, 2, 1, 5, 8, 7, 6, 3],
            [5, 1, 6, 3, 0, 7, 9, 2, 8]
        ]

        r = b.check_legal(board_1, 3, 2, 5)
        self.assertEqual(r, True)
        r = b.check_legal(board_1, 2, 0, 1)
        self.assertEqual(r, True)
        r = b.check_legal(board_1, 4, 8, 4)
        self.assertEqual(r, True)
        r = b.check_legal(board_1, 0, 0, 1)
        self.assertEqual(r, False)
        r = b.check_legal(board_1, 8, 2, 1)
        self.assertEqual(r, False)

    def test_is_solved(self):
        board = [
            [0, 3, 0, 8, 7, 2, 5, 4, 9],
            [2, 7, 5, 6, 9, 4, 8, 3, 1],
            [9, 4, 8, 0, 1, 3, 6, 7, 0],
            [8, 2, 3, 4, 6, 9, 1, 5, 7],
            [7, 5, 4, 2, 8, 1, 3, 9, 6],
            [1, 6, 9, 7, 3, 5, 2, 8, 4],
            [3, 8, 7, 9, 2, 6, 4, 1, 5],
            [4, 9, 2, 1, 5, 8, 7, 6, 3],
            [5, 1, 6, 3, 0, 7, 9, 2, 8]
        ]
        r = b.is_solved(board)
        self.assertEqual(r, False)

        board = [
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
        r = b.is_solved(board)
        self.assertEqual(r, False)
