from collections import deque

SNAKE = "S"
FOOD = "*"
BURROW = "B"
EMPTY = "-"
MOVE_DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), }


def get_terrarium_matrix(square_matrix):
    terrarium_matrix = []
    for row_index in range(square_matrix):
        terrarium_matrix.append([x for x in input()])
    return terrarium_matrix


def get_move_indices(move_command):
    row_index, col_index = MOVE_DIRECTIONS[move_command]
    return row_index, col_index


def get_snake_position(terrarium):
    for row_idx, row in enumerate(terrarium):
        for col_idx, col in enumerate(row):
            if SNAKE in col:
                snake_position = row_idx, col_idx
                return snake_position


def get_burrow_position(terrarium):
    burrow_indices = deque()
    for row_idx, row in enumerate(terrarium):
        for col_idx, col in enumerate(row):
            if BURROW in col:
                burrow_indices.append((row_idx, col_idx))
                return burrow_indices


def get_new_indices(snake_position, move_indices):
    snake_row_pos, snake_col_pos = snake_position
    destination_row, destination_col = move_indices
    new_row_idx, new_col_idx = snake_row_pos + destination_row, snake_col_pos + destination_col
    return (new_row_idx, new_col_idx)


def in_range(terrarium, new_row_idx, new_col_idx):
    return 0 <= new_row_idx < len(terrarium) and 0 <= new_col_idx < len(terrarium)


def get_burrow_pass(burrow_indices_que, new_row_idx, new_col_idx):
    burrow_row_idx, burrow_col_idx = burrow_indices_que.popleft()
    if burrow_row_idx == new_row_idx and burrow_col_idx == new_col_idx:
        burrow_row_idx, burrow_col_idx = burrow_indices_que.popleft()
    return burrow_row_idx, burrow_col_idx


def get_move_commands(terrarium):
    """
    Each turn, you will be given command for the snake’s movement.
    When the snake moves it leaves a trail marked with '.'
    """
    food_count = 0
    snake_position = get_snake_position(terrarium)
    burrow_indices_que = get_burrow_position(terrarium)

    while True:

        move_indices = get_move_indices(input())
        new_row_idx, new_col_idx = get_new_indices(snake_position, move_indices)

        if terrarium[new_row_idx][new_col_idx] == BURROW:
            terrarium[new_row_idx][new_col_idx] = EMPTY
            new_row_idx, new_col_idx = get_burrow_pass(burrow_indices_que, new_row_idx, new_col_idx)

        if not in_range(terrarium, new_row_idx, new_col_idx):
            continue

        empty_row_idx, empty_col_idx = snake_position

        if terrarium[new_row_idx][new_col_idx] == FOOD:
            food_count += 1

        terrarium[empty_col_idx][empty_col_idx] = EMPTY
        terrarium[new_row_idx][new_col_idx] = SNAKE


square_size = int(input())

terrarium = get_terrarium_matrix(square_size)
