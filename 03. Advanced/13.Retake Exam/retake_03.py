from collections import deque


def fill_the_box(height, length, width, *cubes):
    queue = deque()
    box_size = height * length * width
    for el in cubes:
        if el == "Finish":
            break
        else:
            queue.append(int(el))
    while queue:
        cube = queue.popleft()
        if box_size >= cube:
            box_size -= cube
        elif 0 < box_size < cube:
            diff = abs(box_size - cube)
            cube -= diff
            box_size -= diff
            queue.appendleft(cube)
            break
    difference = abs(box_size - sum(queue))
    if box_size > sum(queue):
        return f"There is free space in the box. You could put {difference} more cubes."
    else:
        return f"No more free space! You have {difference} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
