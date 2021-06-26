PLAYER = "P"
EMPTY = "-"
DIRECTION = {
    "up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)
}


def build_field(n):
    """you will be given an integer N for the size of the field with square shape"""
    field_matrix = []
    for _ in range(n):
        field_matrix.append([x for x in input()])
    return field_matrix


def get_player_positoon(field):
    for row_idx in range(len(field)):
        if PLAYER in field[row_idx]:
            col_idx = field[row_idx].index(PLAYER)
            return (row_idx, col_idx)


def is_in_field_range(indices, field):
    row_idx, col_idx = indices
    return 0 <= row_idx < len(field) and 0 <= col_idx < len(field)


def get_new_player_cell(player, direction):
    new_row_idx = player[0] + direction[0]
    new_col_idx = player[1] + direction[1]
    next_player_indices = (new_row_idx, new_col_idx)
    return next_player_indices


def field_update(string_stack, field, old_data, new_data):
    last_player_row_idx, last_player_col_idx = old_data
    new_player_row_idx, new_player_col_idx = new_data
    field[last_player_row_idx][last_player_col_idx] = EMPTY
    if not EMPTY == field[new_player_row_idx][new_player_col_idx]:
        get_string = field[new_player_row_idx][new_player_col_idx]
        string_stack.append(get_string)
    field[new_player_row_idx][new_player_col_idx] = PLAYER
    return string_stack, field


def main(string_stack, field, m):
    """On the next line you receive a number M"""
    player_last_position = None
    for _ in range(m):
        command = input()
        player_position = get_player_positoon(field)
        new_direction = get_new_player_cell(player_position, DIRECTION[command])
        if is_in_field_range(new_direction, field):
            string_stack, field = field_update(string_stack, field, player_position, new_direction)
        elif not is_in_field_range(new_direction, field):
            string_stack.pop()

    return string_stack, field


def print_solution(string_result, field_result):
    print("".join(string_result))
    for row in field_result:
        print("".join(row))


starting_case_string = [x for x in input()]
size_of_field = int(input())
starting_field = build_field(size_of_field)
commands_count = int(input())
string_result, field_result = main(starting_case_string, starting_field, commands_count)

if __name__ == '__main__':
    print_solution(string_result, field_result)
