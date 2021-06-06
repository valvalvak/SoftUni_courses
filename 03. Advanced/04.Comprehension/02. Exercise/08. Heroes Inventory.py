heroes_names = input().split(', ')

inventory = {hero: {} for hero in heroes_names}

command = input()

while not command == "End":

    current_hero, item, cost = command.split("-")
    if item not in inventory[current_hero]:
        inventory[current_hero][item] = int(cost)

    command = input()

# for current_hero in inventory[heroes_names]:
#     all_hero_items_cost = sum(inventory[heroes_names].values())
#     hero_items_count = len(inventory[current_hero])
#     print(f"{current_hero} -> Items: {hero_items_count}, Cost:{all_hero_items_cost}")

print('\n'.join
      (f"{hero} -> Items: {len(inventory[hero])}, Cost: {sum(inventory[hero].values())}" for hero in heroes_names)
      )
