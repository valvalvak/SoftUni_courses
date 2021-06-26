def get_missing_value(args):
    for i in range(min(args), max(args)):
        if i not in args:
            return i


def get_duplicates(args):
    duplicated_vals = []
    for val in args:
        if args.count(val) > 1:
            duplicated_vals.append(val)
    return sorted(set(duplicated_vals))


def numbers_searching(*args):
    missing_value = get_missing_value(args)
    duplicates = get_duplicates(args)
    solution_result = [missing_value, duplicates]

    return solution_result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
