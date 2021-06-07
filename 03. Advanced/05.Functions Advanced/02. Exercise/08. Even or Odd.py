def even_odd(*args):
    nums = args[0:-1]
    if "even" in args:
        return list(filter(lambda x: int(x) % 2 == 0, nums))
    if "odd" in args:
        return list(filter(lambda x: not int(x) % 2 == 0, nums))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
