from collections import deque


def get_splitted():
    """spilt input lists of employees and orders"""
    return [int(x) for x in input().split(", ")]


def are_all_orders_complete(orders):
    if len(orders) <= 0:
        return True
    return False


def todo_pizza_orders(orders, employees):
    """take the first order and the last employee"""

    baked_pizza_counter = 0

    while orders and employees:
        # if are_all_orders_complete(orders):
        #     break

        current_order = orders.popleft()

        if current_order <= 0 or current_order > 10:
            continue

        current_employee = employees.pop()

        if current_order <= current_employee:
            baked_pizza_counter += current_order
            continue

        elif current_order > current_employee:
            orders.appendleft(current_order - current_employee)
            baked_pizza_counter += current_employee

    return orders, employees, baked_pizza_counter


def print_result(orders_lef, employees_left, pizza_count):
    """
    If all orders are successfully completed, print:
    #
    Otherwise, if you ran out of employees and there are still some orders left print:
    """
    if are_all_orders_complete(orders_lef):
        print(f"All orders are successfully completed!")
        print(f"Total pizzas made: {pizza_count}")
        print(f"Employees: {', '.join(map(str, employees_left))}")
    else:
        print(f"Not all orders are completed.")
        print(f"Orders left: {', '.join(map(str, orders_lef))}")


pizza_orders = deque(get_splitted())

employees_order_capacities = deque(get_splitted())

orders, employees, pizza_counter = todo_pizza_orders(pizza_orders, employees_order_capacities)

print_result(orders, employees, pizza_counter)
