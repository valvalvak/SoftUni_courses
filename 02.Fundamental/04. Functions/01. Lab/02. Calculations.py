def calculations(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a // b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


operator_switch = input()
num_a = int(input())
num_b = int(input())

print(calculations(num_a, num_b, operator_switch))
