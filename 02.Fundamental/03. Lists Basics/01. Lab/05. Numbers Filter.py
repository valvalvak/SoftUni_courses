n = int(input())

even = []
odd = []
negative = []
positive = []

for _ in range(n):
    value = int(input())
    if value >= 0:
        positive.append(value)
    if value < 0:
        negative.append(value)
    if value % 2 == 0:
        even.append(value)
    if not value % 2 == 0:
        odd.append(value)
command = input()
if command == "positive":
    print(positive)
elif command == "negative":
    print(negative)
elif command == "even":
    print(even)
else:
    print(odd)
