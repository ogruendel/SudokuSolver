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


def fill_last_num_in_row(board):
    for i, row in enumerate(board):
        if row.count(0) == 1:
            for missing_num in range(1, 10):
                if row.count(missing_num) == 0:
                    board[i][row.index(0)] = missing_num
    return board


def fill_last_num_in_col(board):
    for column in range(0, 9):
        col = []
        for row in board:
            col.append(row[column])

        if col.count(0) == 1:
            for missing_num in range(1, 10):
                if col.count(missing_num) == 0:
                    board[col.index(0)][column] = missing_num

    return board


def fill_last_num_in_block(board):
    for offset in range(0, 9, 3):
        for row_chunk in range(0, 3):
            block = []
            for row in range(0, 3):
                for num in board[row + offset][row_chunk * 3:row_chunk * 3 + 3]:
                    block.append(num)

            if block.count(0) == 1:
                if block.index(0) in range(0, 3):
                    zero_in_block_row = 0
                elif block.index(0) in range(3, 6):
                    zero_in_block_row = 1
                else:
                    zero_in_block_row = 2
                for missing_num in range(1, 10):
                    if block.count(missing_num) == 0:
                        board[zero_in_block_row + offset][board[zero_in_block_row + offset].index(0)] = missing_num
    return board


def is_solved(board):
    for row in board:
        if row.count(0) != 0:
            return False
    return True


def solve(board):
    # TODO
    while not is_solved(board):
        fill_last_num_in_row(board)
        fill_last_num_in_col(board)
        fill_last_num_in_block(board)

