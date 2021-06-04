def read_matrix(rows):
    matrix_build = []

    for i in range(rows):
        matrix_build.append(list(input().split(" ")))

    return matrix_build


def check_if_sub_matrix_exist(character, matrix, row, col, size):
    for r in range(row, row + size):
        for c in range(col, col + size):
            if not character == matrix[r][c]:
                return False
    return True


def sub_matrix_counter(matrix, size):
    counter = 0
    for rows in range(len(matrix) - size + 1):
        for cols in range(len(matrix[rows]) - size + 1):
            current_symbol = matrix[rows][cols]
            if check_if_sub_matrix_exist(current_symbol, matrix, rows, cols, size) is True:
                counter += 1
    return counter


SUB_MATRIX_SQUARE_SIZE = 2

row, col = [int(x) for x in input().split()]

matrix = read_matrix(row)

counter_result = sub_matrix_counter(matrix, SUB_MATRIX_SQUARE_SIZE)

print(counter_result)
