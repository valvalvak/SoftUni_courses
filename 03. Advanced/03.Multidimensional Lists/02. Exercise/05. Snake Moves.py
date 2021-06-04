from collections import deque

row, col = [int(x) for x in input().split(' ')]
snake_as_list_from_string = list(x for x in input())

matrix = []

snake = deque(snake_as_list_from_string.copy())

for r in range(row):
    matrix.append([])
    for c in range(col):
        if r % 2 == 0:
            matrix[r].append(snake[0])
            snake.rotate(-1)
        else:
            matrix[r].insert(0, snake[0])
            snake.rotate(-1)

for r in range(len(matrix)):
    row = []
    for c in range(len(matrix[r])):
        row.append(matrix[r][c])
    print(''.join(x for x in row))