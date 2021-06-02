def read_matrix(rows):
    matrix_build = []

    for i in range(rows):
        matrix_build.append([int(x) for x in input().split(' ')])

    return matrix_build


def matrix_swapping_operations(coomand):
    pass


row, col = [int(x) for x in input().split(' ')]
matrix = read_matrix(row)
command = input()
while not command == "END":
    result = matrix_swapping_operations(matrix)
    command = input()
