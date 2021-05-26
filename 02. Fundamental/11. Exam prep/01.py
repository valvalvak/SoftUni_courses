initial_energy = int(input())

distance = input()
counter_won_battles = 0
is_winner = True

while True:

    if distance == "End of battle":
        break
    distance = int(distance)

    if initial_energy - distance >= 0:
        initial_energy -= distance
        counter_won_battles += 1
        if counter_won_battles % 3 == 0:
            initial_energy += counter_won_battles
    else:
        is_winner = False
        print(f"Not enough energy! Game ends with {counter_won_battles} won battles and {initial_energy} energy")
        break

    distance = input()

if is_winner:
    print(f"Won battles: {counter_won_battles}. Energy left: {initial_energy}")
