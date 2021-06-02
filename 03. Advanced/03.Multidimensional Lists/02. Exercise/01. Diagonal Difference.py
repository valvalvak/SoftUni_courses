def read_matrix(rows):
    matrix_build = []

    for i in range(rows):
        matrix_build.append([int(x) for x in input().split(" ")])

    return matrix_build


def prime_diagonal_sum(matrix):
    result = 0
    size = len(matrix)
    for i in range(size):
        result += matrix[i][i]
    return result


def mirror_diagonal_sum(matrix):
    result = 0
    size = len(matrix)
    for i in range(size):
        result += matrix[i][size - i - 1]
    return result


matrix = read_matrix(int(input()))

print(abs(prime_diagonal_sum(matrix) - mirror_diagonal_sum(matrix)))
