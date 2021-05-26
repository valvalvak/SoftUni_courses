events = input().split("|")

energy = 100
coins = 100
isBakery_over = False
for event in events:
    task, value = event.split("-")
    value = int(value)

    if task == "rest":
        gained_energy = value
        if energy < 100:
            if gained_energy + energy <= 100:
                print(f"You gained {gained_energy} energy.")
                energy += gained_energy
            else:
                difference = abs(gained_energy - (gained_energy + energy - 100))
                print(f"You gained {difference} energy.")
                energy += difference
        else:
            print(f"You gained {0} energy.")
        print(f"Current energy: {energy}.")

    elif task == "order":
        if energy - 30 < 0:
            energy += 50
            print("You had to rest!")
        else:
            print(f"You earned {value} coins.")
            energy -= 30
            coins += value

    else:
        ingredient = task
        if not coins - value <= 0:
            print(f"You bought {ingredient}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            isBakery_over = True
            break

if not isBakery_over:
    print(f"Day completed!\n"f"Coins: {coins}\n"f"Energy: {energy}")
