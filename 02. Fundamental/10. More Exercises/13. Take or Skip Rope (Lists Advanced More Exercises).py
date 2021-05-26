encrypted = input()
non_nums = ""
nums = ""
decrypted = ""
for i in encrypted:
    if not i.isdigit():
        non_nums += i
    else:
        nums += i

take_list = []
skip_list = []
for num in range(len(nums)):
    if num % 2 == 0:
        take_list += nums[num]
    else:
        skip_list += nums[num]

for ele_in in range(len(take_list)):
    index = int(take_list[ele_in])
    decrypted += non_nums[:index]
    non_nums = non_nums[index:]
    for ele_out in range(ele_in, ele_in + 1):
        index = int(skip_list[ele_out])
        non_nums = non_nums[index:]

print(decrypted)
