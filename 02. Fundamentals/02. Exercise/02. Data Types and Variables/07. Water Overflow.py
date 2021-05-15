n = int(input())

capacity = 0

for _ in range(n):
    income = int(input())
    if capacity + income <= 255:
        capacity += income
    else:
        print("Insufficient capacity!")
print(capacity)
