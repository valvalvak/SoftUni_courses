n = int(input())
result = 0
for index in range(1, n + 1):
    char = input()
    digit = ord(char)
    result += digit
print(f"The sum equals: {result}")
