matrix = []
for x in range(4):
    matrix.append([x for x in input()])
print(f"{[[x for x in row] for row in matrix]}", sep="\n")
