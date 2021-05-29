def draw_mattrix(rows):
    mattrix = []

    for i in range(rows):
        mattrix.append([int(x) for x in input().split(" ")])

    return mattrix


input_range = [int(x) for x in input().split(", ")]

mattrix = draw_mattrix(input_range[0])
