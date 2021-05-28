n, m = input().split()
n, m = int(n), int(m)
set_a = set()
set_b = set()
for i in range(n + m):
    if not i > n - 1:
        set_a.add(int(input()))
    else:
        set_b.add(int(input()))
sets_interception = set_a.intersection(set_b)
for unique_item in sets_interception:
    print(unique_item)
