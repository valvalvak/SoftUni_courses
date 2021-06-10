"""
sol1
==============================================
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
# ]
#
# flat = [x for row in matrix for x in row]
#
# print(flat)
==============================================

sol2
==============================================
# flat = []
# for _ in range(int(input())):
#     flat.extend(list(int(x) for x in input().split(', ')))
# print(flat)
"""


def str_to_int():
    strings = input().split(', ')
    return [int(x) for x in strings]


def read_matrix():
    rows_count = int(input())
    return [str_to_int() for _ in range(rows_count)]


def print_solution():
    matrix = read_matrix()
    print([x for row in matrix for x in row])


print_solution()
