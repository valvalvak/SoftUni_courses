def odd_max(tmp_list):
    nums = tmp_list[0]
    index1 = None
    for i in range(len(tmp_list)):
        if tmp_list[i] % 2 != 0 and tmp_list[i] >= nums:
            nums = list2[i]
            index1 = i
    return index1


def odd_min(tmp_list2):
    nums2 = tmp_list2[0]
    index2 = None
    for i in range(len(tmp_list2)):
        if tmp_list2[i] % 2 != 0 and tmp_list2[i] <= nums2:
            nums2 = list2[i]
            index2 = i
    return index2


list1 = [0, 10, 21, 4, 0 , 45, 66, 11, 66]

list2 = [101, 101, 101, 101, 0, 101, 101, 0, 101]

even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos)

# num = list1[0]
# index = None
# for i in range(len(list1)):
#     if list1[i] % 2 == 0 and list1[i] >= num:
#         num = list1[i]
#         index = i
# print(index)

result_max = odd_max(list1)
result_min = odd_min(list1)
if result_max:
    print(result_max)
else:
    print("No max matches")
if result_min:
    print(result_min)
else:
    print("No min matches")
filtered_nums1 = list(el for el in list1 if el % 2 == 0 and not el == 0)
filtered_nums2 = list(el for el in list2 if el % 2 == 0 and not el == 0)
print(filtered_nums1)
print(filtered_nums2)