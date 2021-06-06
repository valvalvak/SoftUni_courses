"""
do not do!:
==========
print([num for num in range(n, m+1) if [dev for dev in range(2, 10+1) if num % dev == 0]])
==========
start = int(input())
end = int(input())
print(
    [x for x in range(start, end + 1)  if any(x % i == 0 for i in range(2, 11))]
)
"""


def is_divisible(number):
    divisible = [num for num in range(2, 11) if number % num == 0]
    return True if divisible else False


def print_numbers(n, m):
    result = [num for num in range(n, m + 1) if is_divisible(num)]
    return result


print(print_numbers(int(input()), int(input())))
