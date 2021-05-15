div_num = int(input())
bound_num = int(input())

n = 0

for n in range(bound_num, 0, -1):
    if n % div_num == 0:
        break
print(n)
