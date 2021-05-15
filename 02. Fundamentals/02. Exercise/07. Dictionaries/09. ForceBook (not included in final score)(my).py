command = input()

result = {}
pipe = " | "
arrow = " -> "

while not command == "Lumpawaroo":
    if pipe in command:
        side, user = command.split(pipe)
        if side not in result:
            result[side] = [user]
        else:
            if user not in result[side]:
                result[side].append(user)
    elif arrow in command:
        user, side = command.split(arrow)
        if side not in result:
            result[side] = [user]
            print(f"{user} joins the {side} side!")
        else:
            for current_side, current_users in result.items():
                if user in current_users:
                    result[current_side].remove(user)
            result[side].append(user)
            print(f"{user} joins the {side} side!")
    command = input()
sorted_result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x[0])))
for sides, users in sorted_result.items():
    if not sorted_result[sides]:
        continue
    else:
        print(f"Side: {sides}, Members: {len(users)}")
    for user in sorted(users):
        print(f"! {user}")
