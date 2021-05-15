words = input().split()
counter = {}
for i in range(len(words)):
    for el in words[i]:
        if el not in counter:
            counter[el] = 1
        else:
            counter[el] += 1
for res in counter:
    print(f"{res} -> {counter[res]}")
