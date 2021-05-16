# from collections import deque
#
# queries = int(input())
#
# queue = deque()
#
# for i in range(queries):
#     current_case = list(map(int, input().split()))
#     current_case = deque(current_case)
#     command = current_case.popleft()
#     if command == 1:
#         queue.append(current_case.pop())
#     elif command == 2:
#         if queue:
#             queue.pop()
#     elif command == 3:
#         print(max(queue))
#     elif command == 4:
#         print(min(queue))
#
# print(", ".join(map(str, reversed(queue))))
queries = int(input())

queue = []
if not 1 <= queries <= 105:
    exit(0)

for i in range(queries):
    current_case = list(map(int, input().split()))
    command = current_case.pop(0)
    if not 1 <= command <= 4:
        continue
    if command == 1:
        value = current_case.pop()
        if 1 <= value <= 109:
            queue.insert(0, value)
    elif command == 2:
        if queue:
            queue.pop()
    elif command == 3:
        if queue:
            print(max(queue))
    elif command == 4:
        if queue:
            print(min(queue))
    # elif command == 3:
    #     if queue:
    #         for x in range(queue.count(max(queue))):
    #             print(max(queue))
    # elif command == 4:
    #     if queue:
    #         for x in range(queue.count(min(queue))):
    #             print(min(queue))

if queue:
    print(", ".join(map(str, queue)))
