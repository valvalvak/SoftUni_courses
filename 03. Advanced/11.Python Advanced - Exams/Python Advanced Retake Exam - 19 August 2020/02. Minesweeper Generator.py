BOMB = "*"
DELTAS = [(-1, -1), (-1, 0), (-1, +1), (0, -1),
          (0, +1), (+1, -1), (+1, 0), (+1, +1), ]


def get_board(n):
    board = []
    for _ in range(n):
        board.append([0] * n)
    return board


def is_in_range(board, row_idx, col_idx):
    return 0 <= row_idx < len(board) and 0 <= col_idx < len(board)


def add_contact_nums(board, row_idx, col_idx):
    for indices in DELTAS:
        next_row = row_idx + indices[0]
        next_col = col_idx + indices[1]
        if not is_in_range(board, next_row, next_col):
            continue
        elif not board[next_row][next_col] == BOMB:
            board[next_row][next_col] += 1
    return board


def add_bombs(board, mines):
    for i in range(mines):
        indices = [int(x) for x in input()[1:-1].split(", ")]
        row_idx, col_idx = indices
        board[row_idx][col_idx] = BOMB
        board = add_contact_nums(board, row_idx, col_idx)
    return board


def print_board(mine_board):
    for row in mine_board:
        print(" ".join([str(x) for x in row]))


if __name__ == '__main__':
    square_matrix = get_board(int(input()))
    mines_count = int(input())
    mine_board = add_bombs(square_matrix, mines_count)
    print_board(mine_board)
