# Function with global vars solution
SYMBOL = "S"
DOTS = "."
DIRS = {
    'up': lambda: move(-1, 0),
    'down': lambda: move(1, 0),
    'left': lambda: move(0, -1),
    'right': lambda: move(0, 1),
}


def search_matrix(matrix, s):
    for row_idx, row in enumerate(matrix):
        for col_idx, char in enumerate(row):
            if char == s:
                return row_idx, col_idx


def is_in_range(new_snake_row_idx, new_snake_col_idx):
    return 0 <= new_snake_row_idx < N and 0 <= new_snake_col_idx < N


def move(delta_row_idx, delta_col_idx):
    global snake_pos, game_over, food_quantity

    snake_row_idx, snake_col_idx = snake_pos
    territory[snake_row_idx][snake_col_idx] = DOTS
    new_snake_row_idx = snake_row_idx + delta_row_idx
    new_snake_col_idx = snake_col_idx + delta_col_idx

    if not is_in_range(new_snake_row_idx, new_snake_col_idx):
        game_over = True
        return

    at_pos = territory[new_snake_row_idx][new_snake_col_idx]
    if at_pos == 'B':
        territory[new_snake_row_idx][new_snake_col_idx] = '.'
        new_snake_row_idx, new_snake_col_idx = search_matrix(territory, 'B')
    elif at_pos == '*':
        food_quantity += 1
        if food_quantity >= 10:
            game_over = True
    territory[new_snake_row_idx][new_snake_col_idx] = 'S'
    snake_pos = (new_snake_row_idx, new_snake_col_idx)


def print_territory():
    print('\n'.join([''.join(row) for row in territory]))


N = int(input())
territory = [list(input()) for _ in range(N)]
snake_pos = search_matrix(territory, SYMBOL)
game_over = False
food_quantity = 0

while not game_over:
    command = input()
    move_fn = DIRS[command]
    move_fn()

if game_over and food_quantity < 10:
    print("Game over!")
else:
    print("You won! You fed the snake.")

print(f'Food eaten: {food_quantity}')

print_territory()
