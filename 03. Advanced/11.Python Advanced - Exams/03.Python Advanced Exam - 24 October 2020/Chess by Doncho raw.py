board = []

# O(N^3)
# for row_index in range(len(board)):
#     for col_index in range(len(board[row_index])):
#         if board[row_index][col_index] == "Q":
#             # run algorithm form possition "Queen"
#             pass


# queens = []
# for row_idx in range(len(board)):
#     for col_idx in range(len(board[row_idx])):
#         if board[row_idx][col_idx] == "Q":
#             queens.append((row_idx, col_idx))


# for queen in queens:
#     pass

# for row_idx in range(len(board)):
#     for col_idx in range(len(board[row_idx])):
#         pass

# def get_queens_beating_kings(board, king):
#     rows_count = len(board)
#     col_count = len(board[0])
#     queens = []
#     (king_row_idx, king_col_idx) = king
#     # -> itteraton
#     for col_idx in range(king_col_idx + 1, col_count):
#         if board[king_row_idx][col_idx] == QUEEN_SYMBOL:
#             queens.append((king_row_idx, col_idx))
#             break
#     # <- itteration
#     for col_idx in range((king_col_idx - 1), -1, -1):
#         if board[king_row_idx][col_idx] == QUEEN_SYMBOL:
#             queens.append((king_row_idx, col_idx))
#             break
#
#     return queens

# return [
#     ['.', '.', '.', '.', '.', '.', '.', '.'],
#     ['Q', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', 'K', '.', '.', '.', 'Q', '.', '.'],
#     ['.', '.', '.', 'Q', '.', '.', '.', '.'],
#     ['Q', '.', '.', '.', 'Q', '.', '.', '.'],
#     ['.', 'Q', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', 'Q', '.'],
#     ['.', 'Q', '.', 'Q', '.', '.', '.', '.'],
# ]
