list_of_integers = input().split()
check_amount = int(input())

arranged_list = [int(x) for x in list_of_integers]
arranged_list.sort()
new_list = []
for digit in range(check_amount):
    num = int(arranged_list[digit])
    if any(num for num in list_of_integers):
        list_of_integers.remove(str(num))
    else:
        continue
new_list = [int(y) for y in list_of_integers]
print(new_list)
