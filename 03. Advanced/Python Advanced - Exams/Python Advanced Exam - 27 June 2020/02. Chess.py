KING_SYMBOL = "K"
QUEEN_SYMBOL = "Q"
BOARD_SIZE = 8
DELTAS = [(-1, -1), (-1, 0), (-1, +1), (0, -1),
          (0, +1), (+1, -1), (+1, 0), (+1, +1), ]


def read_input(board_size):
    board = []
    for _ in range(board_size):
        board.append([x for x in input().split()])
    return board


def find_kings_on_board(board):
    for row_idx in range(len(board)):
        if KING_SYMBOL in board[row_idx]:
            col_idx = board[row_idx].index(KING_SYMBOL)
            return (row_idx, col_idx)


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    cols_count = len(board[0])
    (delta_row, delsta_col) = deltas
    (row_idx, col_idx) = king

    while True:

        if not in_range(row_idx, rows_count) or not in_range(col_idx, cols_count):
            return None

        if board[row_idx][col_idx] == QUEEN_SYMBOL:
            return (row_idx, col_idx)

        row_idx += delta_row
        col_idx += delsta_col


def get_queens_beating_kings(board, king):
    queens_location_list = [search_with_deltas(
        board, king, delta) for delta in DELTAS]
    return [queen_location for queen_location in queens_location_list if queen_location]


def print_result(queens):
    if queens:
        for queen in queens:
            print(list(queen))
    else:
        print("The king is safe!")


board = read_input(BOARD_SIZE)

king = find_kings_on_board(board)

queens = get_queens_beating_kings(board, king)

print_result(queens)
