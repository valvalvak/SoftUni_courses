def solution(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c


num_a = int(input())
num_b = int(input())
num_c = int(input())

print(solution(num_a, num_b, num_c))
