current_version = input().split(".")
next_version = list(map(lambda x: int(x), current_version))
next_version[-1] += 1
for rule in range(len(next_version)-1, 0, -1):
    if next_version[rule] == 9 or next_version[rule] == 10:
        next_version[rule] = 0
        next_version[rule-1] += 1
print(*next_version, sep=".")
