def read_matrix(rows):
    matrix_read = []

    for i in range(rows):
        matrix_read.append([int(x) for x in input().split(" ")])

    return matrix_read


def sum_col_as_list(rows, column, current_matrix):
    column_sums = []
    for col in range(column):
        column_sums.append(int(0))
        for row in range(rows):
            column_sums[col] += current_matrix[row][col]
    return column_sums


# def print_solution(solution):
#     for element in solution:
#         print(element)


given_rows, given_columns = [int(x) for x in input().split(", ")]

matrix = read_matrix(given_rows)

matrix_columns_sums = sum_col_as_list(given_rows, given_columns, matrix)

# print_result = print_solution(matrix_columns_sums)

for element in matrix_columns_sums:
    print(element)
