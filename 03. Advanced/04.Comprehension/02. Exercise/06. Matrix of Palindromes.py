rows, cols = [int(x) for x in input().split()]

matrix = []

first_chr = ord('a')

for row in range(rows):
    matrix.append([])

    for col in range(cols):
        first_letter = chr(row + first_chr)
        mid_letter = chr(row + col + first_chr)

        matrix[row].append(f"{first_letter}{mid_letter}{first_letter}")

print('\n'.join(' '.join([str(x) for x in row]) for row in matrix))
