list_of_str_to_int = [int(x) for x in input().split(", ")]
for i in range(len(list_of_str_to_int)):
    if list_of_str_to_int[i] == 0:
        current_num = list_of_str_to_int[i]
        list_of_str_to_int.remove(list_of_str_to_int[i])
        list_of_str_to_int.append(current_num)
print(list_of_str_to_int)

