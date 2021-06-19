from collections import deque

BUNNY = 'B'
PLAYER = 'P'
PLAYER_TRAIL = "."
DELTAS_DIRECTIONS = {
    "U": (-1, 0),
    "D": (+1, 0),
    "L": (0, -1),
    "R": (0, +1),
}


def read_input(is_test=False):
    if is_test:
        layer = [
            [".", ".", ".", ".", ".", ".", ".", "B"],
            [".", ".", ".", "B", ".", ".", ".", "."],
            [".", ".", ".", ".", "B", ".", ".", "B"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "P", ".", ".", ".", ".", "."],
        ]
        directions = "ULLL"

        return (layer, directions)
    row_count, col_count = [
        int(x) for x in input().split(' ')
    ]
    layer = []
    for _ in range(row_count):
        layer.append(list(input()))
    directions = list(input())
    return (layer, directions)


def matrix_scope(value, max_value):
    return 0 <= value < max_value


def get_bunnies(layer):
    bunnies = []
    for row_idx in range(len(layer)):
        for col_idx in range(len(layer[0])):
            if layer[row_idx][col_idx] == BUNNY:
                bunnies.append((row_idx, col_idx))
    return bunnies


def get_player(lair):
    for row_idx in range(len(lair)):
        if PLAYER in lair[row_idx]:
            col_idx = lair[row_idx].index(PLAYER)
            return (row_idx, col_idx)


def free_cell_check(layer, position):
    row_count = len(layer)
    col_count = len(layer[0])
    (row_idx, col_idx) = position

    return matrix_scope(row_idx, row_count) and matrix_scope(col_idx, col_count) and layer[row_idx][col_idx] != BUNNY


def bunnies_multiply(layer, bunnies):
    for _ in range(len(bunnies)):
        rabbit = bunnies.popleft()
        bunny_multiplication = [
            next_move_direction(rabbit, direction)
            for direction in DELTAS_DIRECTIONS.keys()
        ]
        bunny_multiplication = [
            new_bunnies for new_bunnies in bunny_multiplication if free_cell_check(layer, new_bunnies)
        ]
        for (row_index, col_index) in bunny_multiplication:
            layer[row_index][col_index] = BUNNY
            bunnies.append((row_index, col_index))


def next_move_direction(position, direction):
    (row_idx, col_idx) = position
    (delta_row, delta_col) = DELTAS_DIRECTIONS[direction]
    return row_idx + delta_row, col_idx + delta_col


def is_game_won(layer, player):
    (row_idx, col_idx) = player
    return not matrix_scope(row_idx, len(layer)) or not matrix_scope(col_idx, len(layer[0]))


def is_game_lost(layer, player):
    (row_idx, col_idx) = player
    return layer[row_idx][col_idx] == BUNNY


def print_game(layer, player, player_alive):
    row_idx, col_idx = player
    [print(*row, sep="") for row in layer]
    if player_alive:
        print(f"won: {row_idx} {col_idx}")
    else:
        print(f"dead: {row_idx} {col_idx}")


def game_logic(layer, bunnies, player, directions):
    row_idx, col_idx = player
    bunnies = deque(bunnies)

    for direction in directions:
        bunnies_multiply(layer, bunnies)
        next_row_idx, nex_col_idx = next_move_direction((row_idx, col_idx), direction)

        if is_game_won(layer, (next_row_idx, nex_col_idx)):
            layer[row_idx][col_idx] = PLAYER_TRAIL
            print_game(layer, (row_idx, col_idx), player_alive=True)
            break

        elif is_game_lost(layer, (next_row_idx, nex_col_idx)):
            print_game(layer, (next_row_idx, nex_col_idx), player_alive=False)
            break

        layer[next_row_idx][nex_col_idx] = PLAYER
        layer[row_idx][col_idx] = PLAYER_TRAIL
        row_idx, col_idx = next_row_idx, nex_col_idx


layer, directions = read_input()
bunnies = get_bunnies(layer)
player = get_player(layer)
game_play = game_logic(layer, bunnies, player, directions)
# bunnies_que = deque(bunnies)
# print_game(layer, (0, 0), False)
# print(bunnies_que)
# bunnies_multiply(layer, bunnies_que)
# print_game(layer, (0, 0), False)
# print(bunnies_que)
