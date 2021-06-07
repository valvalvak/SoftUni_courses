def is_even(number):
    return number % 2 == 0


nums = [int(x) for x in input().split()]
print(list(filter(is_even, nums)))
