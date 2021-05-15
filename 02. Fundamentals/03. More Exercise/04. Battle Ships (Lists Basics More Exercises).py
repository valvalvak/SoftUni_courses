rows = int(input())
all_rows = []
ships_counter = 0

for row in range(rows):
    all_rows.append(list(map(int, input().split())))

all_attacks = input().split()

for attack in all_attacks:
    row, col = attack.split("-")
    row = int(row)
    col = int(col)
    if all_rows[row][col] > 0:
        all_rows[row][col] -= 1
        if all_rows[row][col] == 0:
            ships_counter += 1

print(ships_counter)
