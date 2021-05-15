# # nums_as_string = input().split(", ")
# # nums = [int(el) for el in nums_as_string]
# # # nums_map = list(map(lambda el: int(el), nums_as_string))
# # # nums_map_ref = list(map(int, nums_as_string))
# #
# # filtered_nums = [index for index in range(len(nums)) if nums[index] % 2 == 0]
# # # filtered_num_filter = list(map(lambda el: nums.index(el), list(filter(lambda el: el % 2 == 0, nums))))
# # print(filtered_nums)
# *******************************************************************************
# happines = [int(el) for el in input().split()]
# factor = int(input())
# multiplied_hapinnes_by_factor = [num * factor for num in happines]
# # multiplied_hapinnes_by_factor = list(map(lambda num: num*factor, happines))
# avg_happines = sum(multiplied_hapinnes_by_factor) / len(multiplied_hapinnes_by_factor)
#
# happy_employees = [h for h in multiplied_hapinnes_by_factor if h > avg_happines]
#
# # happy_employees = []
# # for h in multiplied_hapinnes_by_factor:
# #     if h >=avg_happines:
# #         happy_employees.append(h)
#
# # happy_employees = list(filter(lambda h: h > avg_happines, multiplied_hapinnes_by_factor))
#
# half_n = len(multiplied_hapinnes_by_factor) / 2
#
# if len(happy_employees) >= half_n:
#     print(f"Score: {len(happy_employees)}/{len(multiplied_hapinnes_by_factor)}. Employees are happy!")
# else:
#     print(f# for index in range(len(items)):
# #     if index == len(items) -1:
# #         print(f"{items[index]}")
# #     else:
# #         print(f"{items[index]}, ", end='')
# # group = []
# # # while 0 <= len(group):
# # #     while len(list_as_ints) > 0:
# # #         list_to_print = [num for num in list_as_ints if num <= group]
# # #         for el in list_to_print:
# # #             list_as_ints.remove(el)
# # #         print(f"Group of {group}'s: {list_to_print}")
# # #         group += 10"Score: {len(happy_employees)}/{len(multiplied_hapinnes_by_factor)}. Employees are not happy!")
temp_list = [1, 2, 1]
temp_list_z = [int(x) for x in temp_list]
temp_list_z.reverse()
result_list = []
for i in range(len(temp_list)):
    if temp_list[i] == temp_list_z[i]:
        print("True", end=" ")
    else:
        print("False", end=" ")
