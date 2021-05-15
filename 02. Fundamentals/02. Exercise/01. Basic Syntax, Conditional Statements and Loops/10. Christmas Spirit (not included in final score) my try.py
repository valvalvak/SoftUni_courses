quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

days_counter = 0
spirit = 0
budget = 0

while not days <= 0:
    days_counter += 1
    if days_counter % 11 == 0:
        quantity += 2
    if days_counter % 2 == 0:
        budget += ornament_set * quantity
        spirit += 5
    if days_counter % 3 == 0:
        budget += tree_skirt * quantity + tree_garlands * quantity
        spirit += 13
    if days_counter % 5 == 0:
        budget += tree_lights * quantity
        spirit += 17
        if days_counter % 3 == 0:
            spirit += 30
    if days_counter % 10 == 0:
        spirit -= 20
        budget += tree_skirt + tree_garlands + tree_lights
        if days == 1:
            spirit -= 30
    days -= 1

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
