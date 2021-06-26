PLAYER = "P"
WALL = "X"
DIRECTION = {
    "up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)
}


def build_field():
    """
    On the first line, you will be given a number representing the size of the field with square shape.
    On the next few lines, you will be given a field with:
    -> One player randomly placed in it and marked with symbol "P";
    -> Numbers for coins placed at different positions of the field
    -> Walls marked with "X".
    """
    while True:
        try:
            n = int(input())
            field_matrix = []
            for _ in range(n):
                field_matrix.append([x for x in input()])
            return field_matrix
        except ValueError:
            print("Wrong value! Must be an intiger! Please try gain", int(input()))
            continue


def get_player_position(field):
    for row_idx in range(len(field)):
        if PLAYER in field[row_idx]:
            col_idx = field[row_idx].index(PLAYER)
            return row_idx, col_idx


def is_in_field_range(indices, field):
    row_idx, col_idx = indices
    return 0 <= row_idx < len(field) and 0 <= col_idx < len(field)


def get_new_player_cell(player, direction_index):
    new_row_idx = player[0] + direction_index[0]
    new_col_idx = player[1] + direction_index[1]
    new_player_indices = (new_row_idx, new_col_idx)
    return new_player_indices


def field_update(field, old_position, new_position):
    last_player_row_idx, last_player_col_idx = old_position
    new_player_row_idx, new_player_col_idx = new_position

    return None


def main(field, ):
    """
    After the field state, you will be given commands for the players movement.
    Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it.
    If the player goes out of the field or he hits a wall, he loses the game and his coins are reduced to 50%
    and ROUNDED DOWN TO THE NEXT LOWES NUMBER. **** THE PROGRAM ENDS ***
    Otherwise, the player has to collect AT LEAST ___100 COINS TO WIN___ the game.
    """

    while True:
        command = input()
        if command not in DIRECTION:
            continue
        player_position = get_player_position(field)

    return field


def print_solution(string_result, field_result):
    print("".join(string_result))
    for row in field_result:
        print("".join(row))


starting_field = build_field()
string_result, field_result = main(starting_case_string, starting_field, commands_count)

if __name__ == '__main__':
    print_solution(string_result, field_result)
