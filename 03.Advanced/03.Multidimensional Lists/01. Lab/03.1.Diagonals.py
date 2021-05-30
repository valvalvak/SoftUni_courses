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


def sum_sub_prime_diagonal_1(matrix):
    result = 0
    size = len(matrix)
    for row in range(size):
        for col in range(size):
            if row < col:  # to exclude prime diagonal add '='
                break
            result += matrix[row][col]  # size - row - 1 for mirror
    return result


def sum_sub_prime_diagonal_2(matrix):
    result = 0
    size = len(matrix)
    for row in range(size):
        for col in range(row):  # to include prime diagonal add range '+ 1'
            result += matrix[row][col]  # size - row - 1 for mirror
    return result


def sum_top_prime_diagonal_1(matrix):
    result = 0
    size = len(matrix)
    for row in range(size):
        for col in range(size):
            if col > row:  # to include prime diagonal add '='
                result += matrix[row][col]  # size - row - 1 for mirror
    return result


def sum_top_prime_diagonal_2(matrix):
    result = 0
    size = len(matrix)
    for row in range(size):
        for col in range(row, size):  # to include prime diagonal add range '+ 1'
            result += matrix[row][col]  # size - row - 1 for mirror
    return result


matrix = read_matrix(int(input()))

print(prime_diagonal_sum(matrix))

print(mirror_diagonal_sum(matrix))

print(sum_sub_prime_diagonal_1(matrix))

print(sum_sub_prime_diagonal_2(matrix))

print(sum_top_prime_diagonal_1(matrix))

print(sum_top_prime_diagonal_2(matrix))
