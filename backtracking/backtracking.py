def print_board(board):
    for i, row in enumerate(board):
        x = ""
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if num != 0:
                x += str(num) + " "
            else:
                x += "  "
            if (j + 1) % 3 == 0 and j != 8:
                x += "| "
        print(x)
    print('\n')


def check_legal(board, pos_x, pos_y, val):
    return check_legal_in_row(board, pos_y, val) and check_legal_in_col(board, pos_x, val) and check_legal_in_box(board,
                                                                                                                  pos_x,
                                                                                                                  pos_y,
                                                                                                                  val)


def check_legal_in_row(board, pos_y, val):
    if board[pos_y].count(val) == 1:
        return False
    else:
        return True


def check_legal_in_col(board, pos_x, val):
    col = []
    for i in range(9):
        col.append(board[i][pos_x])
    if col.count(val) == 1:
        return False
    else:
        return True


def check_legal_in_box(board, pos_x, pos_y, val):
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


def is_solved(board):
    for row in board:
        for i in range(1, 10):
            if row.count(i) != 1 or row.count(i) == 0:
                return False
    return True


def solve(board):
    for pos_y in range(9):
        for pos_x in range(9):
            if board[pos_y][pos_x] == 0:
                for num in range(1, 10):
                    if check_legal(board, pos_x, pos_y, num):
                        board[pos_y][pos_x] = num
                        print_board(board)
                        if is_solved(board):
                            quit()
                        solve(board)
                        board[pos_y][pos_x] = 0
                return
