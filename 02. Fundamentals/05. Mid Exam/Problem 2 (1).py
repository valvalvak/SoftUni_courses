main_list = input().split(" ")
command = input()
while not command == "end":
    case_list = command.split(" ")
    start_value = 0
    range_value = 0
    if case_list[0] == "reverse":
        start_value = abs(int(case_list[2]))
        range_value = start_value + abs(int(case_list[4]))
        main_list = main_list[:start_value]+main_list[start_value:range_value][::-1]+main_list[range_value:]
    elif case_list[0] == "sort":
        start_value = abs(int(case_list[2]))
        range_value = start_value + abs(int(case_list[4]))
        sorted_list = main_list[start_value:range_value]
        sorted_list.sort()
        main_list = main_list[:start_value]+sorted_list+main_list[range_value:]
    elif case_list[0] == "remove":
        range_value = abs(int(case_list[1]))
        main_list = main_list[range_value:]
    command = input()
print(", ".join(main_list))
