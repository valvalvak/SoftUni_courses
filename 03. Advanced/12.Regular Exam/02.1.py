MATRIX_SIZE = 5
PLAYER = "A"
TARGET = "x"
EMPTY = "."
MOVE_DIRECTION = {
    "up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)
}
TARGET_SHOTS_INDICES = [

]


def build_field(n):
    """you will be given an integer N for the size of the field with square shape"""
    field_matrix = []
    for r in range(n):
        field_matrix.append([x for x in input().split(" ")])
    return field_matrix


def get_player_position(field):
    player_indices = None
    target_count = 0
    for row_idx in range(len(field)):
        for col_idx in range(len(field[row_idx])):
            if field[row_idx][col_idx] == PLAYER:
                player_indices = (row_idx, col_idx)
            if field[row_idx][col_idx] == TARGET:
                target_count += 1

    return player_indices, target_count


def is_in_range(field, next_row, next_col):
    return 0 <= next_row < len(field) and 0 <= next_col < len(field)


def get_aim_cell(player, direction):
    aim_row_idx, aim_col_idx = MOVE_DIRECTION[direction]
    new_row_idx = player[0] + aim_row_idx
    new_col_idx = player[1] + aim_row_idx
    next_player_indices = (new_row_idx, new_col_idx)
    return next_player_indices


def get_to_move_cell(player, direction, steps):
    aim_row_idx, aim_col_idx = MOVE_DIRECTION[direction]
    new_row_idx = player[0] + aim_row_idx * steps
    new_col_idx = player[1] + aim_col_idx * steps
    next_player_indices = (new_row_idx, new_col_idx)
    return next_player_indices


def get_update_move_field(field, next_row_idx, next_col_idx, player_position):
    if is_in_range(field, next_row_idx, next_col_idx) and field[next_row_idx][next_col_idx] == EMPTY:
        field[player_position[0]][player_position[1]] = EMPTY
        field[next_row_idx][next_col_idx] = PLAYER
    return field, next_row_idx, next_col_idx


def target_shot(field, row, col):
    TARGET_SHOTS_INDICES.append([row, col])
    field[row][col] = EMPTY


def found_a_target(field, player_pos, direction):
    dir_row, dir_col = MOVE_DIRECTION[direction]
    aim_row, aim_col = dir_row + player_pos[0], dir_col + player_pos[1]

    while True:
        if not is_in_range(field, aim_row, aim_col):
            return False
        if field[aim_row][aim_col] == TARGET:
            target_shot(field, aim_row, aim_col)
            return True
        aim_row, aim_col = aim_row + dir_row, aim_col + dir_col


def are_targes_shot(all_targes, targets_shot):
    return all_targes <= targets_shot


def main(field, lines_count, all_targets=0, targets_shot=0):
    mem_player_pos = []
    for _ in range(lines_count):
        command = input()
        if not mem_player_pos:
            player_position, all_targets = get_player_position(field)
            mem_player_pos.append(player_position)
        else:
            player_position = mem_player_pos[-1]

        if command.startswith("shoot"):
            _, direction = command.split(" ")
            if found_a_target(field, player_position, direction):
                targets_shot += 1

        elif command.startswith("move"):
            _, direction, steps = command.split(" ")
            steps = int(steps)
            next_row_idx, next_col_idx = get_to_move_cell(player_position, direction, steps)
            if is_in_range(field, next_row_idx, next_col_idx):
                field, row, col = get_update_move_field(field, next_row_idx, next_col_idx, player_position)
                mem_player_pos.append([row, col])

        if are_targes_shot(all_targets, targets_shot):
            return all_targets, targets_shot

    return all_targets, targets_shot


def print_solution(all_targets, targets_shot, TARGET_SHOTS_INDICES):
    if targets_shot < all_targets:
        print(f"Training not completed! {all_targets - targets_shot} targets left.")
    else:
        print(f"Training completed! All {all_targets} targets hit.")
    for location in TARGET_SHOTS_INDICES:
        print(location)


starting_field = build_field(MATRIX_SIZE)
lines_count = int(input())
all_targets, targets_shot = main(starting_field, lines_count)
print_solution(all_targets, targets_shot, TARGET_SHOTS_INDICES)
