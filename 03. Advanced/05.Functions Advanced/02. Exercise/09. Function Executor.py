def sum_numbers(num1, num2, num3):
    return num1 + num2 + num3


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for function, arguments in args:
        f_result = function(*arguments)
        result.append(f_result)
    return result


print(func_executor((sum_numbers, (3, 3, 3)), (multiply_numbers, (2, 4)), (sum_numbers, (3, 3, 3))))
