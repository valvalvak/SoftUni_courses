task = input()
Peter_social_book = {}
while not task == "Log out":
    task_data = task.split(": ")
    enter = task_data[0]
    user = task_data[1]
    if enter == "New follower":
        if user not in Peter_social_book:
            Peter_social_book[user] = {"likes": 0, "comments": 0}
    elif enter == "Like":
        count = int(task_data[2])
        if user not in Peter_social_book:
            Peter_social_book[user] = {"likes": count, "comments": 0}
        else:
            Peter_social_book[user]["likes"] += count
    elif enter == "Comment":
        if user not in Peter_social_book:
            Peter_social_book[user] = {"likes": 0, "comments": 1}
        else:
            Peter_social_book[user]["comments"] += 1
    elif enter == "Blocked":
        if user not in Peter_social_book:
            print(f"{user} doesn't exist.")
        else:
            Peter_social_book.pop(user)
    task = input()

print(f"{len(Peter_social_book)} followers")
for name, values in sorted(Peter_social_book.items(), key=lambda x: (-(x[1]["likes"] + x[1]["comments"]), x[0])):
    result = values["likes"] + values["comments"]
    print(f"{name}: {result}")
