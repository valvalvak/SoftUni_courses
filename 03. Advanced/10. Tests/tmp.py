# def read_matrix(rows):
#     matrix_read = []
#
#     for i in range(rows):
#         matrix_read.append([int(x) for x in input().split(" ")])
#
#     return matrix_read
#
# def count_matrix_cols(rows, column, matrix):
#     column_sums = []
#     for col in range(column):
#         column_sums.append(int(0))
#         for row in range(rows):
#             column_sums[col] += matrix[row][col]
#     return column_sums
#
# def print_solution(solution):
#     for element in solution:
#         print(element)
#
# given_rows, given_colomuns = [int(x) for x in input().split(", ")]
#
# matrix = read_matrix(given_rows)
#
# print_result = print_solution(count_matrix_cols(given_rows, given_colomuns, matrix))
#
# a = [20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10]
# a.reverse()
# print(a)


a = ["O", "O", "O"]
if a.count("O") == len(a):
    print("True")
else:
    print("False")
