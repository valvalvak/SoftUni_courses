n = int(input())

max_intersection = ()

for i in range(n):
    first, second = input().split("-")

    start1, end1 = first.split(",")
    start2, end2 = second.split(",")

    set1 = range(int(start1), int(end1) + 1)
    set2 = range(int(start2), int(end2) + 1)

    current_intersection = set(set1).intersection(set(set2))

    if len(current_intersection) > len(max_intersection):
        max_intersection = current_intersection

print(f"Longest intersection is {list(max_intersection)} with length {len(max_intersection)}")
