def is_divisible(number):
    divisible = [num for num in range(2, 11) if number % num == 0]
    return True if divisible else False


def print_numbers(n, m):
    result = [num for num in range(n, m + 1) if is_divisible(num)]
    return result


print(print_numbers(int(input()), int(input())))

"""
not to do!
print([num for num in range(n, m+1) if [dev for dev in range(2, 10+1) if num % dev == 0]])
"""
