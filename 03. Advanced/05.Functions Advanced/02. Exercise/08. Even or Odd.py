def even_odd(*args):
    if "even" in args:
        return list(filter(lambda x: int(x) % 2 == 0, args[0:-1]))
    if "odd" in args:
        return list(filter(lambda x: not int(x) % 2 == 0, args[0:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
