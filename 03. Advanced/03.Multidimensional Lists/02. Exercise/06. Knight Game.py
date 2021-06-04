def read_board():
    matrix = []
    n = int(input())

    for _ in range(n):
        matrix.append(list(input()))

    return matrix


def sub_matrix_positions_to_chek(row, col):
    positions = [
        (row - 2, col + 1),
        (row - 1, col + 2),
        (row + 1, col + 2),
        (row + 2, col + 1),
        (row + 2, col - 1),
        (row + 1, col - 2),
        (row - 1, col - 2),
        (row - 2, col - 1),
    ]
    return positions


def knights_are_attacking_each_other(matrix):
    knight_positions = find_all_knights(matrix)
    rows_indices_range = len(matrix) - 1
    cols_indices_range = len(matrix[0]) - 1
    for row, col in knight_positions:
        positions_to_check = sub_matrix_positions_to_chek(row, col)

        for position in positions_to_check:
            pos_row, pos_col = position

            if not (0 <= pos_row <= rows_indices_range):
                continue
            elif not (0 <= pos_col <= cols_indices_range):
                continue
            if matrix[pos_row][pos_col] == 'K':
                return True

    return False


def find_all_knights(matrix):
    positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'K':
                positions.append((i, j))

    return positions


def calculate_aggression(matrix, knight_positions):
    aggression_scores = {}
    rows_indices_range = len(matrix) - 1
    cols_indices_range = len(matrix[0]) - 1
    for pos in knight_positions:
        row, col = pos
        positions_to_check = sub_matrix_positions_to_chek(row, col)

        attacked_count = 0
        for attacked_row, attacked_col in positions_to_check:
            if not (0 <= attacked_row <= rows_indices_range):
                continue
            elif not (0 <= attacked_col <= cols_indices_range):
                continue
            if matrix[attacked_row][attacked_col] == 'K':
                attacked_count += 1
                aggression_scores[(row, col)] = attacked_count

    return aggression_scores


def find_max_aggression(aggression_scores):
    max_so_far = None
    max_pos = None

    for pos, aggression in aggression_scores.items():
        if max_so_far is None or max_so_far < aggression:
            max_so_far = aggression
            max_pos = pos

    return max_pos


def main():
    matrix = read_board()

    deleted_knights_count = 0
    while knights_are_attacking_each_other(matrix) is True:
        knight_positions = find_all_knights(matrix)  # [(0, 0), (1, 1)]
        aggression_scores = calculate_aggression(matrix, knight_positions)  # {(0, 0): 5}

        row, col = find_max_aggression(aggression_scores)

        matrix[row][col] = '0'
        deleted_knights_count += 1

    print(deleted_knights_count)


main()