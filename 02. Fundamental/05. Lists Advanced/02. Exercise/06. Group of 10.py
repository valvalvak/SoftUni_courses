list_of_nums = list(map(int, input().split(", ")))
tens_high_range = 0
list_result = []
list_of_nums_len = len(list_of_nums)
max_value = max(list_of_nums)
while not list_of_nums_len <= 0:
    tens_high_range += 10
    tens_low_range = tens_high_range - 10
    for num in range(len(list_of_nums)):
        if list_of_nums[num] in range(tens_low_range + 1, tens_high_range + 1):
            list_result.append(list_of_nums[num])
    list_of_nums_len -= len(list_result)
    print(f"Group of {tens_high_range}'s: {list_result}")
    if max_value in list_result:
        break
    list_result.clear()
