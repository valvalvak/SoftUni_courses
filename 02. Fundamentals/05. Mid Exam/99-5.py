array_list = [int(el) for el in input().split()]
command_info = input()
while not command_info == 'end':
    data = command_info.split()
    index_1 = int(data[1])
    index_2 = int(data[2])

    if data[0] == 'swap':
        array_list[index_1], array_list[index_2] = array_list[index_2], array_list[index_1]

    elif data[0] == 'multiply':
        multi = array_list[index_1] * array_list[index_2]
        array_list.pop(index_1)
        array_list.insert(index_1, multi)

    elif data[0] == 'decrease':
        for n in array_list:
            n -= 1
    command_info = input()

    if data[0] == 'end':
        print(', '.join(str(ele) for ele in array_list))

