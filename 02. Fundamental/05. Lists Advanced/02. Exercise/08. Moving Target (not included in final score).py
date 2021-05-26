targets_list = [int(x) for x in input().split(" ")]
list_length = len(targets_list) - 1
command = input()
target_value = 0
while not command == "End":
    action, index, value = command.split(" ")
    index = int(index)
    value = int(value)
    target_value = 0
    if action == "Shoot":
        if not index > list_length and not index < 0:
            target_value = targets_list[index]
            target_value -= value
            if target_value <= 0:
                targets_list.remove(targets_list[index])
                list_length = len(targets_list) - 1
            else:
                targets_list[index] = int(target_value)
    if action == "Add":
        if not index > list_length and not index < 0:
            targets_list.insert(index, value)
            list_length = len(targets_list) - 1
        else:
            print("Invalid placement!")
    if action == "Strike":
        if not index > list_length and not index < 0 and not list_length // 2 - value < 0 and not value > index:
            left_part = targets_list[:(index - value)]
            right_part = targets_list[(index + value + 1):]
            targets_list.remove(targets_list[index])
            targets_list = left_part + right_part
            list_length = len(targets_list) - 1
        else:
            print("Strike missed!")
    command = input()

targets_list = [str(x) for x in targets_list]
print("|".join(targets_list))
