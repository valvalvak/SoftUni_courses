from collections import deque

BOARD_SIZE = 7


def get_players_que():
    players_que = deque([x for x in input().split(", ")])
    return players_que


def manage_players_results(player_queue):
    players_points = {}
    player_throw_counter = {}
    for player in player_queue:
        players_points[player] = 501
        player_throw_counter[player] = 0
    return players_points, player_throw_counter


def build_dartboard_matrix(board_size):
    board_matrix = [[board_cell for board_cell in input().split(" ")] for _ in range(board_size)]
    return board_matrix


def are_valid_indices(board, row_idx, col_idx):
    board_size = len(board)
    return 0 <= row_idx < board_size and 0 <= col_idx < board_size


def recieve_throw_coordinates():
    indices = [int(x) for x in input()[1:-1].split(", ")]
    return tuple(indices)


def print_winner(winner, throws):
    print(f"{winner} won the game with {throws} throws!")


def calculate_d_or_t_points(board, row_idx, col_idx):
    first_current_row = int(board[row_idx][0])
    last_current_row = int(board[row_idx][-1])
    top_current_column = int(board[0][col_idx])
    bottom_current_column = int(board[-1][col_idx])
    calculation = first_current_row + last_current_row + top_current_column + bottom_current_column

    if board[row_idx][col_idx] == "D":
        return calculation * 2
    return calculation * 3


def game_play(board, players):
    points, counter = manage_players_results(players)
    while True:
        row_idx, col_idx = recieve_throw_coordinates()
        current_player = players.popleft()
        counter[current_player] += 1

        if not are_valid_indices(board, row_idx, col_idx):
            players.append(current_player)
            continue

        if board[row_idx][col_idx] == "B":
            return current_player, counter[current_player]

        elif board[row_idx][col_idx] == "D":
            points[current_player] -= calculate_d_or_t_points(board, row_idx, col_idx)

        elif board[row_idx][col_idx] == "T":
            points[current_player] -= calculate_d_or_t_points(board, row_idx, col_idx)

        else:
            points[current_player] -= int(board[row_idx][col_idx])

        if points[current_player] <= 0:
            return current_player, counter[current_player]

        players.append(current_player)


player_que = get_players_que()
dartboard = build_dartboard_matrix(BOARD_SIZE)
winner, throws_count = game_play(dartboard, player_que)
print_winner(winner, throws_count)
