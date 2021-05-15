def winner_item(legendary_item):
    legendary_item = ""
    if "shards" == winner:
        legendary_item = "Shadowmourne obtained!"
    elif "fragments" == winner:
        legendary_item = "Valanyr obtained!"
    elif "motes" == winner:
        legendary_item = "Dragonwrath obtained!"
    return legendary_item


command = input().lower().split()
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
winner = ""
mark = False

while not mark:
    for i in range(0, len(command), 2):
        key, value = command[i + 1], command[i]
        if key == "shards" or key == "fragments" or key == "motes":
            key_materials[key] += int(value)
            if key_materials[key] >= 250:
                winner = key
                print(winner_item(winner))
                key_materials[key] -= 250
                mark = True
                break
        else:
            if key not in junk_materials:
                junk_materials[key] = value
            else:
                junk_materials[key] += value
    if mark:
        break
    command = input().lower().split()

sorted_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
for key, val in sorted_materials.items():
    print(f"{key}: {val}")

sorted_junk = dict(sorted(junk_materials.items(), key=lambda x: x[0]))
for j, v in sorted_junk.items():
    print(f"{j}: {v}")
