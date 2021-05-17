n = int(input())

stack = []

counter = 1

for _ in range(n):
    counter += 1
    if counter > 105:
        break
    current_case = list(map(int, input().split()))
    command = current_case.pop(0)
    if command == 1:
        num = current_case[0]
        if 1 <= num <= 109:
            stack.insert(0, num)
    elif command == 2:
        if stack:
            stack.pop(0)
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))
if stack:
    print(", ".join(map(str, stack)))
else:
    print(stack)
