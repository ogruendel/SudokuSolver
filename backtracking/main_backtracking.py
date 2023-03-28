import backtracking

board = [
    [0, 0, 4, 0, 2, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 9, 0, 7, 1],
    [0, 9, 6, 0, 0, 0, 4, 0, 5],
    [5, 0, 1, 0, 6, 0, 0, 0, 0],
    [7, 0, 8, 9, 1, 2, 3, 0, 4],
    [3, 0, 9, 4, 0, 5, 6, 1, 8],
    [0, 1, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 3, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 2, 3, 0, 0, 4, 6]
]

fixed = backtracking.fix_positions(board)
print(fixed)
backtracking.solve(board, fixed)
