def order_sum(order_type, amount):
    result = None
    if order_type == "coffee":
        result = amount * 1.50
    elif order_type == "water":
        result = amount * 1.00
    elif order_type == "coke":
        result = amount * 1.40
    elif order_type == "snacks":
        result = amount * 2.00
    return result


order = input()
quantity = float(input())

print(f"{order_sum(order, quantity):.2f}")
