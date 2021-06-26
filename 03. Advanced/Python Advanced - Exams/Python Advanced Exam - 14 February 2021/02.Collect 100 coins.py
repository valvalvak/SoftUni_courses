from math import floor

PLAYER = "P"
WALL_SYMBOL = "X"
COINS_TARGET = 100
DIRECTION = {
    "up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)
}


def build_field(n):
    """
    On the first line, you will be given a number representing the size of the field with square shape.
    On the next few lines, you will be given a field with:
    -> One player randomly placed in it and marked with symbol "P";
    -> Numbers for coins placed at different positions of the field
    -> Walls marked with "X".
    """
    field_matrix = []
    for _ in range(n):
        field_matrix.append([x for x in input().split(" ")])
    return field_matrix


def get_player_position(field, last_positions):
    if not last_positions:
        for row_idx in range(len(field)):
            if PLAYER in field[row_idx]:
                col_idx = field[row_idx].index(PLAYER)
                return row_idx, col_idx
    else:
        last_position = last_positions[-1]
        last_row_index = last_position[0]
        last_col_index = last_position[-1]
        return last_row_index, last_col_index


def is_next_step_in_range(field, next_row, next_col):
    return 0 <= next_row < len(field) and 0 <= next_col < len(field)


def next_step(player_row, player_col, command):
    dir_row, dir_col = DIRECTION[command]
    new_row_idx = player_row + dir_row
    new_col_idx = player_col + dir_col
    return new_row_idx, new_col_idx


def is_next_step_wall(field, nex_row_idx, next_col_idx, wall_symbol):
    if not field[nex_row_idx][next_col_idx] == wall_symbol:
        return True


def is_game_won(coins):
    return coins >= COINS_TARGET


def main(field):
    """
    After the field state, you will be given commands for the players movement.
    Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it.
    If the player goes out of the field or he hits a wall, he loses the game and his coins are reduced to 50%
    and ROUNDED DOWN TO THE NEXT LOWES NUMBER. **** THE PROGRAM ENDS ***
    Otherwise, the player has to collect AT LEAST ___100 COINS TO WIN___ the game.
    """
    positions = []
    coins = 0

    while True:
        if is_game_won(coins):
            return coins, positions

        command = input()
        if command not in DIRECTION:
            continue

        player_row_idx, player_col_index = get_player_position(field, positions)
        nex_row_idx, next_col_idx = next_step(player_row_idx, player_col_index, command)

        if not is_next_step_in_range(field, nex_row_idx, next_col_idx):
            return floor(coins / 2), positions

        if not is_next_step_wall(field, nex_row_idx, next_col_idx, WALL_SYMBOL):
            return floor(coins / 2), positions

        coins += int(field[nex_row_idx][next_col_idx])
        positions.append((nex_row_idx, next_col_idx))


def print_solution(coins, positions):
    """
    Output
    If the player won the game, print: "You won! You've collected {total_coins} coins."
    If the player loses the game, print: "Game over! You've collected {total_coins} coins."
    Collected coins have to be rounded down to the next-lowest number.
    The field positions from which the player has collected coins as lists:
    Your path:
    [{row_position1}{column_position1}]
    [{row_position2}{column_position2}]
    [{row_position3}{column_position3}] and so on...
    """
    if is_game_won(coins):
        print(f"You won! You've collected {coins} coins.")
    else:
        print(f"Game over! You've collected {coins} coins.")
    print("Your path:")
    for path in positions:
        print(f"{[*path]}")


starting_field = build_field(int(input()))
coins, positions = main(starting_field)

if __name__ == '__main__':
    print_solution(coins, positions)
