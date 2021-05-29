rows, columns = [int(x) for x in input().split(", ")]

# matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

# print(f"{sum(x for x in matrix)}\n{matrix}")

matrix = []
sum_result = 0

for _ in range(rows):
    lines = [int(x) for x in input().split(", ")]
    sum_result += sum(lines)
    matrix.append(lines)

print(f"{sum_result}\n{matrix}")
