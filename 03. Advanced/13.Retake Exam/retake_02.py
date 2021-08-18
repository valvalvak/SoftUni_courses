ALLICE = "A"
EMPTY_SLOT = "."
PATH_TRAIL = "*"
RABBIT_HOLE = "R"
MOVE_DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
TARGET_POINTS = 10


def make_matrix(value):
    matrix_res = []
    allice_position = ()
    rabbit_hole_position = ()
    for row in range(value):
        matrix_res.append([x for x in input().split(" ")])
        if ALLICE in matrix_res[row]:
            allice_position = (row, matrix_res[row].index(ALLICE))
        elif RABBIT_HOLE in matrix_res[row]:
            rabbit_hole_position = (row, matrix_res[row].index(RABBIT_HOLE))

    return matrix_res, allice_position, rabbit_hole_position


def movement(command, move_directions):
    for move in move_directions:
        if move == command:
            move_coordinates = move_directions[move]
            return move_coordinates


def get_next_pos(allice_position, move_coordinates):
    allice_row, allice_col = allice_position
    move_row, move_col = move_coordinates
    return allice_row + move_row, allice_col + move_col


def in_range(row, col, matrix):
    max_index = len(matrix) - 1
    return 0 <= row <= max_index and 0 <= col <= max_index


def get_breack_case(next_move_row, next_move_col, matrix):
    if not in_range(next_move_row, next_move_col, matrix):
        return True
    elif matrix[next_move_row][next_move_col] == RABBIT_HOLE:
        matrix[next_move_row][next_move_col] = PATH_TRAIL
        return True


def main(matrix, allice_position):
    points = 0
    last_row_pos, last_col_pos = allice_position
    allice = (last_row_pos, last_col_pos)
    while True:
        if points >= TARGET_POINTS:
            print("She did it! She went to the party.")
            break
        else:
            command = input()
        next_move_row, next_move_col = get_next_pos(allice, movement(command, MOVE_DIRECTIONS))
        if get_breack_case(next_move_row, next_move_col, matrix):
            print("Alice didn't make it to the tea party.")
            break
        elif matrix[next_move_row][next_move_col] == EMPTY_SLOT:
            allice = (next_move_row, next_move_col)
            matrix[last_row_pos][last_col_pos] = PATH_TRAIL
            matrix[next_move_row][next_move_col] = PATH_TRAIL
        elif matrix[next_move_row][next_move_col] == PATH_TRAIL:
            allice = (next_move_row, next_move_col)
        elif matrix[next_move_row][next_move_col].isdigit():
            points += int(matrix[next_move_row][next_move_col])
            allice = (next_move_row, next_move_col)
            matrix[last_row_pos][last_col_pos] = PATH_TRAIL
            matrix[next_move_row][next_move_col] = PATH_TRAIL
    return points, matrix


def print_matrix_solution(matrix):
    for row in matrix:
        print(f"{' '.join([x for x in row])}")


matrix, allice_position, rabbit_hole_position = make_matrix(int(input()))
points, new_matrix = main(matrix, allice_position)
print_matrix_solution(new_matrix)
