def get_magic_triangle(n):
    row = [1]
    triangle = [[1]]

    for idx in range(n - 1):
        row = [sum(x) for x in zip([0] + row, row + [0])]
        triangle.append(row)

    return triangle


print(get_magic_triangle(4))
