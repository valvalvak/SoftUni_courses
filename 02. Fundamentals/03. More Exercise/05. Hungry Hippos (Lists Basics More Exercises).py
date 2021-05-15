def find_neighbours(lst, block_lst, x, y):
    if x - 1 in range(len(lst)):
        if lst[x - 1][y] == 1:
            if [x - 1, y] not in block_lst:
                block_lst.append([x - 1, y])
                block_lst = find_neighbours(lst, block_lst, x - 1, y)
    if x + 1 in range(len(lst)):
        if lst[x + 1][y] == 1:
            if [x + 1, y] not in block_lst:
                block_lst.append([x + 1, y])
                block_lst = find_neighbours(lst, block_lst, x + 1, y)
    if y - 1 in range(len(lst[0])):
        if lst[x][y - 1] == 1:
            if [x, y - 1] not in block_lst:
                block_lst.append([x, y - 1])
                block_lst = find_neighbours(lst, block_lst, x, y - 1)
    if y + 1 in range(len(lst[0])):
        if lst[x][y + 1] == 1:
            if [x, y + 1] not in block_lst:
                block_lst.append([x, y + 1])
                block_lst = find_neighbours(lst, block_lst, x, y + 1)
    return block_lst


n_rows = int(input())
matrix = []
for _ in range(n_rows):
    inp = [int(x) for x in input().split()]
    matrix.append(inp)

all_blocks = []
block = []
count_b = 0
for m in range(len(matrix)):
    for n in range(len(matrix[0])):
        if matrix[m][n] == 1 and [m, n] not in all_blocks:
            block.append([m, n])
            block = find_neighbours(matrix, block, m, n)
            all_blocks += block
            block = []
            count_b += 1

print(count_b)
