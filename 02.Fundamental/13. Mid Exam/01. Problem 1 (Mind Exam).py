days = int(input())
players = int(input())
group_energy = float(input())
water = float(input())
food = float(input())

all_water = days * players * water
all_food = days * players * food

days_counter = 0
isTrue = True
while not group_energy <= 0:
    energy_spent = float(input())
    if group_energy - energy_spent <= 0:
        print(f"You will run out of energy. You will be left with {all_food:.2f} food and {all_water:.2f} water.")
        isTrue = False
        break
    group_energy = group_energy - energy_spent
    days_counter += 1
    if days_counter >= 2 and days_counter % 2 == 0:
        group_energy *= 1.05
        all_water *= 0.70
    if days_counter >= 3 and days_counter % 3 == 0:
        group_energy *= 1.10
        all_food -= all_food / players
    if days_counter == days:
        break
if isTrue:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
