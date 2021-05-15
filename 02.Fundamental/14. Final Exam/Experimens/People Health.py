command = input()
all_dict = {}
while not command == "Results":
    command = command.split(":")
    order = command[0]
    if order == "Add":
        person = command[1]
        health = int(command[2])
        energy = int(command[3])
        if person in all_dict:
            all_dict[person]['health'] += health
        else:
            all_dict[person] = {'health': health, 'energy': energy}
    elif order == "Attack":
        attacker = command[1]
        defender = command[2]
        damage = int(command[3])
        if attacker in all_dict and defender in all_dict:
            all_dict[defender]['health'] -= damage
            if all_dict[defender]['health'] <= 0:
                del all_dict[defender]
                print(f"{defender} was disqualified!")
            all_dict[attacker]['energy'] -= 1
            if all_dict[attacker]['energy'] == 0:
                del all_dict[attacker]
                print(f"{attacker} was disqualified!")
    elif order == "Delete":
        username = command[1]
        if username in all_dict:
            del all_dict[username]
        if username == "All":
            all_dict.clear()
    command = input()
sorted_all_dict = sorted(all_dict.items(), key=lambda kvp: (-kvp[1]['health'], kvp[0]))
print(f"People count: {len(all_dict)}")
for key, value in sorted_all_dict:
    print(f"{key} - {value['health']} - {value['energy']}")
