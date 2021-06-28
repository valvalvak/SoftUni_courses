def generete_empty_triangle(size):
    triangle = []

    for i in range(size):
        triangle.append([0] * (i + 1))

    return triangle


def generate_magic_triangle(triangle):
    triangle[0][0] = 1
    size = len(triangle)
    for row_index, row in enumerate(triangle):
        for col_index, col in enumerate(row):
            left = right = 0
            if (row_index, col_index) == (0, 0):
                continue

            if (0 <= row_index - 1 < size) and (0 <= col_index - 1 < len(triangle[row_index - 1])):
                left = triangle[row_index - 1][col_index - 1]
            if (0 <= row_index - 1 < size) and (0 <= col_index < len(triangle[row_index - 1])):
                right = triangle[row_index - 1][col_index]

            triangle[row_index][col_index] = left + right

    return triangle


def get_magic_triangle(n):
    triangle = generete_empty_triangle(n)
    generate_magic_triangle(triangle)

    return triangle


def test():
    print(get_magic_triangle(3))
    print(get_magic_triangle(5))


if __name__ == '__main__':
    test()
