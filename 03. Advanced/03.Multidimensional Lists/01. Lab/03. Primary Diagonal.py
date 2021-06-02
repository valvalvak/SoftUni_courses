def read_matrix(rows):
    matrix_build = []

    for i in range(rows):
        matrix_build.append([int(x) for x in input().split(" ")])

    return matrix_build


def prime_diagonal_sum(matrix):
    result = 0
    for row in range(len(matrix)):
        result += matrix[row][row]
    return result


matrix = read_matrix(int(input()))

print(prime_diagonal_sum(matrix))
