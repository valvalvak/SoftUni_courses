def get_magic_triangle(n):
    triangle = []

    for i in range(n):
        triangle.append([[0] * (i * 1)])

    return triangle


def test():
    print(get_magic_triangle(3) == [[0], [0, 0], [0, 0, 0]])


if __name__ == '__main__':
    test()
