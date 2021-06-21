class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        super().__init__(f"{value} is negative")


def vadiate_positive_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ValueCannotBeNegativeError(number)
    return print(f"Numbers are positive{numbers}")


numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 5, 6]
numbers3 = [1, 1, 1, 1, 2]

vadiate_positive_numbers(numbers1)
vadiate_positive_numbers(numbers2)
vadiate_positive_numbers(numbers3)
print("End of demo test")
