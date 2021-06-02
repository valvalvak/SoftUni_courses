def read_matrix(rows):
    matrix_build = []

    for i in range(rows):
        matrix_build.append([x for x in input()])

    return matrix_build


def find_if_symbol_in_matrix(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == symbol:
                return (row, col)
    return False


matrix = read_matrix(int(input()))

searching_symbol = input()

searching_symbol_result = find_if_symbol_in_matrix(matrix, searching_symbol)

if searching_symbol_result:
    print(searching_symbol_result)
else:
    print(f"{searching_symbol} does not occur in the matrix")
