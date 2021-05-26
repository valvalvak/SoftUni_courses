def factorial_num_one(a):
    res_b = 1
    a = int(a)
    for i in range(a, 0, -1):
        res_b *= i
    return res_b


def factorial_num_two(b):
    res_a = 1
    b = int(b)
    for i in range(b, 0, -1):
        res_a *= i
    return res_a


def solution(one, two):
    return factorial_num_one(one) // factorial_num_two(two)


num_one = input()
num_two = input()

result = solution(num_one, num_two)

print(f"{result:.2f}")
