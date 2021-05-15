from collections import deque

queries = int(input())

queue = deque()

for i in range(queries):
    current_case = list(map(int, input().split()))
    current_case = deque(current_case)
    command = current_case.popleft()
    if command == 1:
        queue.append(current_case.pop())
    elif command == 2:
        if queue:
            queue.pop()
    elif command == 3:
        print(max(queue))
    elif command == 4:
        print(min(queue))

result = ""
while queue:
    result += str(queue.pop()) + " "
print(result.strip())
