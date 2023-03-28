def fix_positions(board):
    fixed_positions = []
    for row_pos, row in enumerate(board):
        for col_pos, num in enumerate(row):
            fixed_pos = []
            if num != 0:
                fixed_pos.append(row_pos)
                fixed_pos.append(col_pos)
                fixed_positions.append(fixed_pos)
    return fixed_positions


def solve(board, fixed):
    for row_pos, row in enumerate(board):
        for col_pos, num in enumerate(row):
            if [row_pos, col_pos] not in fixed:
                for i in range(1, 10):
                    # TODO
                    return


def check_legal(board, row, col):
    check_legal_in_row(board, row, col)
    check_legal_in_col(board, row, col)
    check_legal_in_box(board, row, col)


def check_legal_in_row(board, pos_row, pos_col):
    to_check = board[pos_row][pos_col]
    if to_check == 0 or board[pos_row].count(to_check) != 1:
        return False
    else:
        return True


def check_legal_in_col(board, pos_row, pos_col):
    to_check = board[pos_row][pos_col]
    col = []
    for i in range(0, 9):
        col.append(board[i][pos_col])
    if to_check == 0 or col.count(to_check) != 1:
        return False
    else:
        return True


def check_legal_in_box(board, pos_row, pos_col):
    box = []
    # TODO
