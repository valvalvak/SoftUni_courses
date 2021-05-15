command = input()
current_list = []
result = []
sorted_list = []
while not command == "End":
    current_list.append(command)
    sorted_list = sorted(current_list)
    command = input()
for el in range(len(set(sorted_list))):
    current_task = str(sorted_list[el]).split("-")
    if int(current_task[0]) == 0:
        continue
    if int(current_task[0]) > 10:
        break
    else:
        result.append(current_task[1])
print(result)
