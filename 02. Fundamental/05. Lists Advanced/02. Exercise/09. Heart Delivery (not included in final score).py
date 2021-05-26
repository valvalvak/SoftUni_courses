neighborhood = [int(x) for x in input().split("@")]
command = input()
hearts = 2
current_house = 0
while not command == "Love!":
    jump_step = int(command.split(" ")[1])
    if current_house + jump_step >= len(neighborhood):
        current_house = 0
    else:
        current_house += jump_step
    if neighborhood[current_house] == 0:
        print(f"Place {current_house} already had Valentine's day.")
    else:
        neighborhood[current_house] -= 2
        if neighborhood[current_house] == 0:
            print(f"Place {current_house} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {current_house}.")
if neighborhood.count(0) == len(neighborhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - neighborhood.count(0)} places.")
