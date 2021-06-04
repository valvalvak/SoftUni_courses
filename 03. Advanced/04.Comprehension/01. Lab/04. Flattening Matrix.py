l = []
for _ in range(int(input())):
    l.extend(list(int(x) for x in input().split(', ')))
print(l)
