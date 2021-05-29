n = int(input())

result = set()

for i in range(n):
    first, second = input().split("-")

    start1, end1 = first().split(",")
    start2, end2 = second().split(",")

    set1 = range(start1, end1 + 1)
    set2 = range(start1, end1 + 1)

    result.add(list(set(set1).intersection(set2)))
print(result)
