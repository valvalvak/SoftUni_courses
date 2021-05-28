n = int(input())
set_result = set()
for _ in range(n):
    current_row = input().split(" ")
    for el in current_row:
        set_result.add(el)

for el in set_result:
    print(el)
