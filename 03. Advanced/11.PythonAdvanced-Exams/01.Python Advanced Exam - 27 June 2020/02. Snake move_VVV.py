SNAKE = "S"
FOOD = "*"
BURROW = "B"
TRAIL = "."
MOVE_DIRECTIONS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1), }


def get_terrarium_matrix(square_matrix):
    terrarium_matrix = []
    for row_index in range(square_matrix):
        terrarium_matrix.append([x for x in input()])
    return terrarium_matrix


def get_snake_idx_position(terrarium):
    for row_idx, row in enumerate(terrarium):
        for col_idx, col in enumerate(row):
            if SNAKE in col:
                snake_position = (row_idx, col_idx)
                return snake_position


def get_exit_burrow_idx_position(terrarium):
    """
    There might also be a lair on the territory.
    The lair has two burrows.
    They are marked with the letter - 'B'.
    redactor: this function will rise only if furs burrow is found, which will be replaced with EMPTY,
    so we need only the exit indices.
    """
    for row_idx, row in enumerate(terrarium):
        for col_idx, col in enumerate(row):
            if BURROW in col:
                return (row_idx, col_idx)


def get_move_direction_indices(move_command):
    """Move commands will be: "up", "down", "left", "right"."""
    row_index, col_index = MOVE_DIRECTIONS[move_command]
    return (row_index, col_index)


def get_destination_cell_indices(snake_position, move_indices):
    snake_row_pos, snake_col_pos = snake_position
    destination_row, destination_col = move_indices
    new_row_idx, new_col_idx = snake_row_pos + destination_row, snake_col_pos + destination_col
    return (new_row_idx, new_col_idx)


def are_indices_in_range(terrarium, new_row_idx, new_col_idx):
    return 0 <= new_row_idx < len(terrarium) and 0 <= new_col_idx < len(terrarium)


def play_snake_moves(terrarium):
    """
    Each turn, you will be given command for the snake’s movement.
    When the snake moves it leaves a trail marked with '.'
    """
    food_quantity = 0
    snake_position = get_snake_idx_position(terrarium)

    while True:

        move_direction_indices = get_move_direction_indices(input())
        new_row_idx, new_col_idx = get_destination_cell_indices(snake_position, move_direction_indices)
        last_row_pos, last_col_pos = snake_position
        terrarium[last_row_pos][last_col_pos] = TRAIL

        if not are_indices_in_range(terrarium, new_row_idx, new_col_idx):
            print("Game over!")
            return terrarium, food_quantity

        if terrarium[new_row_idx][new_col_idx] == BURROW:
            terrarium[new_row_idx][new_col_idx] = TRAIL
            burrow_exit = get_exit_burrow_idx_position(terrarium)
            new_row_idx, new_col_idx = burrow_exit

        elif terrarium[new_row_idx][new_col_idx] == FOOD:
            food_quantity += 1

        snake_position = (new_row_idx, new_col_idx)
        terrarium[new_row_idx][new_col_idx] = SNAKE

        if food_quantity >= 10:
            print("You won! You fed the snake.")
            return terrarium, food_quantity


def print_food_quantity_result(terrarium, food_quatity):
    print(f"Food eaten: {food_quatity}")
    for row in terrarium:
        print("".join(map(str, row)))


if __name__ == '__main__':
    square_size = int(input())
    terrarium = get_terrarium_matrix(square_size)
    terrarium, food_quatity = play_snake_moves(terrarium)
    print_food_quantity_result(terrarium, food_quatity)
