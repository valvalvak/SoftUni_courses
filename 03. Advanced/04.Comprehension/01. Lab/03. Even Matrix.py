"""
=============================================================================================
n = int(input())
print([list(int(num) for num in input().split(', ') if int(num) % 2 == 0) for _ in range(n)])
=============================================================================================
even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(even_matrix)
"""


def str_to_int():
    strings = input().split(', ')
    return [int(x) for x in strings]


def read_matrix():
    rows_count = [int(x) for x in input().split(", ")]
    return [str_to_int() for _ in range(len(rows_count))]


def print_solution():
    matrix = read_matrix()
    print([x for row in matrix for x in row])


print_solution()
