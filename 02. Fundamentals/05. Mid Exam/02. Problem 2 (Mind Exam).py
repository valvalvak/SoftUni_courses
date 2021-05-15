biscuits = input().split(", ")
command = input()

while not command == "Eat":
    command_data = command.split()
    action = command_data[0]
    biscuit = command_data[1]
    if len(command_data) == 3:
        index = int(command_data[2])
    if action == "Update-Any":
        if biscuit in biscuits:
            index = biscuits.index(biscuit)
            biscuits[index] = "Out of stock"
    elif action == "Remove":
        if 0 <= index < len(biscuits):
            biscuits[index] = biscuit
    elif action == "Update-Last":
        biscuits[-1] = biscuit
    elif action == "Rearrange":
        if biscuit in biscuits:
            biscuits.remove(biscuit)
            biscuits.append(biscuit)

    command = input()

sorted_biscuits = [bisc for bisc in biscuits if not bisc == "Out of stock"]
print(*sorted_biscuits)