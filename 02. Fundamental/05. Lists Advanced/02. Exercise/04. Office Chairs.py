n = int(input())

result = 0

for chairs in range(1, n + 1):
    taken_n_rest = input().split(" ")
    current_difference = len(taken_n_rest[0]) - int(taken_n_rest[1])
    result += current_difference
    if len(taken_n_rest[0]) < int(taken_n_rest[1]):
        print(f"{abs(current_difference)} more chairs needed in room {chairs}")
    else:
        continue
if not result < 0:
    print(f"Game On, {result} free chairs left")
