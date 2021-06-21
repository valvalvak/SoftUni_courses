def max_numbers(numbers):
    best_number = numbers[0]

    for number in numbers:
        if best_number < number:
            best_number = number

    return best_number


def max_numbers_rec(numbers):
    if len(numbers) == 1:
        return numbers[0]

    x = numbers[-1]
    y = max_numbers_rec(numbers[:-1])

    return x if y < x else y


print(max_numbers([1, 2, 3, 4, 5]))

print(max_numbers_rec([1, 2, 3, 4, 5]))
