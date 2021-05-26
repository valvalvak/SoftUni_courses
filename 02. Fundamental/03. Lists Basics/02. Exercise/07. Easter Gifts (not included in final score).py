list_of_gifts = input().split(" ")
command = input()
while not command == "No Money":
    task = command.split(" ")
    if task[0] == "OutOfStock":
        for i in range(len(list_of_gifts)):
            if task[1] == list_of_gifts[i]:
                list_of_gifts.remove(task[1])
                list_of_gifts.insert(i, "None")
    if task[0] == "Required":
        index = int(task[2])
        if not index > len(list_of_gifts) - 1 and not index < 0:
            list_of_gifts[index] = task[1]
    if task[0] == "JustInCase":
        list_of_gifts[-1] = task[1]
    command = input()
new_list = []
for n in range(len(list_of_gifts)):
    if list_of_gifts[n] == "None":
        continue
    else:
        new_list.append(list_of_gifts[n])

print(" ".join(new_list))
