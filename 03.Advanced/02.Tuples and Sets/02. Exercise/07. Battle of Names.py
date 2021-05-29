n = int(input())

odds = set()
evens = set()

for i in range(1, n + 1):
    name = input()
    current_letter_sum = sum(ord(x) for x in name) // i

    if not current_letter_sum % 2 == 0:
        odds.add(current_letter_sum)
    else:
        evens.add(current_letter_sum)

if sum(odds) == sum(evens):
    print(*odds.union(evens), sep=", ")  # print the union values, separated by ", ".
elif sum(odds) > sum(evens):
    print(*odds.difference(evens), sep=", ")  # print the different values, separated by ", ".
elif sum(odds) < sum(evens):
    print(*odds.symmetric_difference(evens), sep=", ")  # print the symmetric different values, separated by ", ".
