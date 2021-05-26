league_size = int(input())
adventure_days = int(input())
coins = 0
day_counter = 1
while not adventure_days <= 0:
    if day_counter % 15 == 0:
        league_size += 5
    if day_counter >= 10 and day_counter % 10 == 0:
        league_size -= 2
    coins += 50 - league_size * 2
    if day_counter % 3 == 0:
        coins -= league_size * 3
    if day_counter % 5 == 0:
        coins += league_size * 20
        if day_counter % 3 == 0:
            coins -= league_size * 2
    day_counter += 1
    adventure_days -= 1
print(f"{league_size} companions received {coins // league_size} coins each.")
