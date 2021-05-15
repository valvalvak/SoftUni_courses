def sum_of_even_and_odd_numbers(a):
    string_list = [int(i) for i in str(a)]
    even_sum = 0
    odd_sum = 0
    for number in range(len(string_list)):
        if int(string_list[number]) % 2 == 1:
            odd_sum += int(string_list[number])
        else:
            even_sum += int(string_list[number])
    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return result


value = input()
print(sum_of_even_and_odd_numbers(value))
