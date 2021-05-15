def exchange(nums_list, index):
    result = nums_list[index + 1:] + nums_list[:index + 1]
    return result


def find_max_num(nums_list, odd_or_even):
    index = None
    current_num = nums_list[0]
    if odd_or_even == "odd":
        for odd_max in range(len(nums_list)):
            value = nums_list[odd_max]
            if not value % 2 == 0 and value >= current_num:
                current_num = value
                index = odd_max
    else:
        for even_max in range(len(nums_list)):
            value = nums_list[even_max]
            if value % 2 == 0 and value >= current_num:
                current_num = value
                index = even_max
    if index is None:
        return "No matches"
    return index


def find_min_num(nums_list, odd_or_even):
    index = None
    current_num = nums_list[0]
    if odd_or_even == "odd":
        for odd_max in range(len(nums_list)):
            value = nums_list[odd_max]
            if not value % 2 == 0 and value <= current_num:
                current_num = value
                index = odd_max
    else:
        for even_max in range(len(nums_list)):
            value = nums_list[even_max]
            if value % 2 == 0 and value <= current_num:
                current_num = value
                index = even_max
    if index is None:
        return "No matches"
    return index


def first_or_last(task, nums_list, count, odd_or_even):
    if odd_or_even == "odd":
        filtered_nums = list(odd_el for odd_el in nums_list if not odd_el % 2 == 0)
    else:
        filtered_nums = list(even_el for even_el in nums_list if even_el % 2 == 0)
    if task == "first":
        return filtered_nums[:count]
    else:
        return filtered_nums[len(filtered_nums) - count:]


nums = [int(x) for x in input().split()]


command_data = input()
counter = 1

while not command_data == "end":
    command_data = command_data.split()
    command = command_data[0]
    if command == "exchange":
        i = int(command_data[1])
        if 0 <= i <= len(nums) - 1:
            nums = exchange(nums, i)
        else:
            print("Invalid index")
    elif command == "max":
        odd_or_even = command_data[1]
        print(find_max_num(nums, odd_or_even))
    elif command == "min":
        odd_or_even = command_data[1]
        print(find_min_num(nums, odd_or_even))
    elif command == "first" or command == "last":
        count = int(command_data[1])
        odd_or_even = command_data[2]
        if count > len(nums) or count < 0:
            print("Invalid count")
        else:
            print(first_or_last(command, nums, count, odd_or_even))

    if counter + 1 == 51:
        break
    command_data = input()
    counter += 1
print(nums)
