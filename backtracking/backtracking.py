def fix_positions(board):
    fixed_positions = []
    for pos_y, row in enumerate(board):
        for pos_x, num in enumerate(row):
            fixed_pos = []
            if num != 0:
                fixed_pos.append(pos_x)
                fixed_pos.append(pos_y)
                fixed_positions.append(fixed_pos)
    return fixed_positions


def check_legal(board, pos_x, pos_y, val):
    check_legal_in_row(board, pos_y, val)
    check_legal_in_col(board, pos_x, val)
    check_legal_in_box(board, pos_x, pos_y, val)


def check_legal_in_row(board, pos_y, val):
    if board[pos_y].count(val) >= 1:
        return False
    else:
        return True


def check_legal_in_col(board, pos_x, val):
    col = []
    for i in range(9):
        col.append(board[i][pos_x])
    if col.count(val) >= 1:
        return False
    else:
        return True


def check_legal_in_box(board, pos_x, pos_y, val):
    # TODO
    box = []
    if pos_y / 3 < 1:
        y = 0
    elif pos_y / 3 < 2:
        y = 3
    else:
        y = 6

    if pos_x / 3 < 1:
        x = 0
    elif pos_x / 3 < 2:
        x = 3
    else:
        x = 6

    for i in range(3):
        for j in range(3):
            box.append(board[i + y][j + x])
    if val in box:
        return False
    else:
        return True


def solve(board, fixed):
    # TODO
    for pos_x in range(9):
        for pos_y in range(9):
            if [pos_x, pos_y] not in fixed:
                for num in range(1, 10):
                    if check_legal(board, pos_x, pos_y, num):
                        board[pos_x][pos_y] = num
