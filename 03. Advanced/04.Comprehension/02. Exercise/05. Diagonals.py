def read_matrix(rows):
    matrix_build = []
    split_case = ", "

    for i in range(rows):
        matrix_build.append([int(x) for x in input().split(split_case)])

    return matrix_build


def get_prime_diagonal_list(matrix):
    size = len(matrix)
    pd_list = ([x for x in [matrix[i][i] for i in range(size)]])
    return pd_list


def get_mirror_diagonal_list(matrix):
    size = len(matrix)
    md_list = ([x for x in [matrix[i][size - i - 1] for i in range(size)]])
    return md_list


matrix = read_matrix(int(input()))

prime_diagonal_list = get_prime_diagonal_list(matrix)
print(f"First diagonal: {', '.join([str(x) for x in prime_diagonal_list])}. Sum: {sum(prime_diagonal_list)}")

mirror_diagonal_list = get_mirror_diagonal_list(matrix)
print(f"Second diagonal: {', '.join([str(x) for x in mirror_diagonal_list])}. Sum: {sum(mirror_diagonal_list)}")
