data = {}

line = input()
while not line == "Log out":
    tokens = line.split(": ")
    command = tokens[0]
    user = tokens[1]
    if command == "New follower":
        if user not in data:
            data[user] = {"likes": 0, "comments": 0}
    elif command == "Like":
        count = int(tokens[2])
        if user not in data:
            data[user] = {"likes": count, "comments": 0}
        else:
            data[user]["likes"] += count
    elif command == "Comment":
        if user not in data:
            data[user] = {"likes": 0, "comments": 1}
        else:
            data[user]["comments"] += 1
    elif command == "Blocked":
        if user not in data:
            print(f"{user} doesn't exist.")
        else:
            data.pop(user)

    line = input()

print(f"{len(data)} followers")
for name, values in sorted(data.items(), key=lambda kvp: (-(kvp[1]["likes"] + kvp[1]["comments"]), kvp[0])):
    total = values["likes"] + values["comments"]
    print(f"{name}: {total}")
