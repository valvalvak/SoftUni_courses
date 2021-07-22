def build_triangele(n):
    matrix = [[1] * x for x in range(1, n + 1)]
    return matrix


def cells_sum(magic_triangle, row_index, col_index):
    left_cell = magic_triangle[row_index - 1][col_index - 1]
    right_cell = magic_triangle[row_index - 1][col_index]
    return left_cell + right_cell


def get_magic_triangle(triangle):
    magic_triangle = build_triangele(triangle)
    rows = len(magic_triangle)
    for row_index in range(2, rows):
        current_row = (len(magic_triangle[row_index]) - 1)
        for col_index in range(1, current_row):
            magic_triangle[row_index][col_index] = cells_sum(magic_triangle, row_index, col_index)

    return magic_triangle


print(get_magic_triangle(4))
