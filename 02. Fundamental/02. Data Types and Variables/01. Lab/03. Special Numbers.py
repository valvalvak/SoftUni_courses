special_number = int(input())

for n in range(1, special_number + 1):
    sum_of_num = 0
    digits = n
    while digits > 0:
        sum_of_num += digits % 10
        digits = int(digits / 10)
    if (sum_of_num == 5) or (sum_of_num == 7) or (sum_of_num == 11):
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")
