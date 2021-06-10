n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

line = input()
while not line == "END":

    command, row, col, val = line.split()
    row_index, col_index, value = int(row), int(col), int(val)

    if not (0 <= row_index < n) or not (0 <= col_index < n):
        print("Invalid coordinates")
        line = input()
        continue

    if command == "Add":
        matrix[row_index][col_index] += value
    elif command == "Subtract":
        matrix[row_index][col_index] -= value

    line = input()

print('\n'.join([' '.join([str(x) for x in row]) for row in matrix]))
