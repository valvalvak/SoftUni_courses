def exchange(nums_list, index):
    first_part = nums_list[index + 1:]
    second_part = nums_list[:index + 1]
    result = first_part + second_part
    return result


def find_max_num(nums_list, odd_or_even):
    # TODO find index from the whole list
    if odd_or_even == "odd":
        filtered_nums = list(el for el in nums_list if not el % 2 == 0)
    else:
        filtered_nums = list(el for el in nums_list if el % 2 == 0)
    if not filtered_nums:
        return "No matches"
    # TODO find index from the whole list
    max_element = max(filtered_nums)
    index = len(filtered_nums) - filtered_nums[::-1].index(max_element) - 1
    return index


def find_min_num(nums_list, odd_or_even):
    if odd_or_even == "odd":
        filtered_nums = list(el for el in nums_list if not el % 2 == 0)
    else:
        filtered_nums = list(el for el in nums_list if el % 2 == 0)
    if not filtered_nums:
        return "No matches"
    # TODO find index from the whole list
    min_element = min(filtered_nums)
    index = len(filtered_nums) - filtered_nums[::-1].index(min_element) - 1
    return index


def find_first(nums_list, count, odd_or_even):
    if odd_or_even == "odd":
        filtered_nums = list(el for el in nums_list if not el % 2 == 0)
    else:
        filtered_nums = list(el for el in nums_list if el % 2 == 0)
    if 0 < len(filtered_nums) < count:
        return "Invalid count"
    return filtered_nums[:count]


def find_last(nums_list, count, odd_or_even):
    if odd_or_even == "odd":
        filtered_nums = list(el for el in nums_list if not el % 2 == 0)
    else:
        filtered_nums = list(el for el in nums_list if el % 2 == 0)
    if 0 < len(filtered_nums) < count:
        return "Invalid count"
    return filtered_nums[:count][::-1]


nums = [int(x) for x in input().split()]

command_data = input()

while not command_data == "end":
    command_data = command_data.split()
    command = command_data[0]
    if command == "exchange":
        i = int(command_data[1])
        if not i > len(nums) - 1:
            nums = exchange(nums, i)
        else:
            print("Invalid index")
    elif command == "max":
        odd_or_even = command_data[1]
        print(find_max_num(nums, odd_or_even))
    elif command == "min":
        odd_or_even = command_data[1]
        print(find_min_num(nums, odd_or_even))
    elif command == "first":
        count = int(command_data[1])
        odd_or_even = command_data[2]
        print(find_first(nums, count, odd_or_even))
    elif command == "last":
        count = int(command_data[1])
        odd_or_even = command_data[2]
        print(find_first(nums, count, odd_or_even))

    command_data = input()
print(nums)
