from collections import deque


def add_solution(main_list, other_params):
    command, params_list = other_params
    pass


def remove_solution(main_list, other_params):
    pass


def list_manipulator(*args):
    main_list, command, *other_params = args
    main_list = deque(main_list)
    if command == "add":
        main_list = add_solution(main_list, other_params)
    elif command == "remove":
        main_list = remove_solution(main_list, other_params)

    pass


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
