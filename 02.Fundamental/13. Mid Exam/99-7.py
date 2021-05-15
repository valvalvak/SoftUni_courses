action = command.split()[0]
if action == "Loot":
    loot_item = [el for el in command.split() if el != action]
    for el in loot_item:
        if el not in treasure:
            treasure.insert(0, el)

    # if "Loot" in command:
    #     command = command.split()
    #     command.remove("Loot")
    #     for el in command:
    #         if el not in treasure:
    #             treasure.insert(0, el)
