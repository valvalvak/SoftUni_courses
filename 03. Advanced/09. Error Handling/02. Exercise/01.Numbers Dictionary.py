BREAK_COMMANDS = ("Search", "Remove", "End")


def homework_exeption_errors(current_error):
    return current_error


numbers_dictionary = {}


def is_int_current_input(check_if_number):
    return int(check_if_number)


try:
    while True:
        key = input()
        if key in BREAK_COMMANDS:
            break

        number = input()
        if not is_int_current_input(number):
            raise homework_exeption_errors(ValueError)
        else:
            numbers_dictionary[key] = number

    while True:
        key = input()
        if key in BREAK_COMMANDS:
            break

        if key in numbers_dictionary:
            print(numbers_dictionary[key])

    while True:
        key = input()
        if key in BREAK_COMMANDS:
            break

        if key not in numbers_dictionary:
            raise homework_exeption_errors(KeyError)

        else:
            del numbers_dictionary[key]

except homework_exeption_errors(ValueError):
    print("The variable number must be an integer")

except homework_exeption_errors(KeyError):
    print("Number does not exist in dictionary")

print(numbers_dictionary)
