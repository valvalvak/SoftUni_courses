from collections import deque


def get_males_and_females_ques():
    queue = deque(int(el) for el in input().split())
    return queue


males = get_males_and_females_ques()
females = get_males_and_females_ques()

queue = []
matches = 0

for el in range(len(males)):
    queue.append(males.pop())

while queue and females:
    i = 0
    if queue[i] <= 0:
        queue.pop(i)
        continue
    elif females[i] <= 0:
        females.popleft()
        continue
    if queue[i] % 25 == 0:
        queue.pop(i)
        if queue:
            queue.pop(i + 1)
    elif females[i] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()

    if queue[i] == females[i]:
        matches += 1
        queue.pop(i)
        females.popleft()
    else:
        females.popleft()
        queue[i] -= 2

print(f'Matches: {matches}')
if queue:
    queue = list(queue)
    print(f"Males left: {', '.join(map(str, queue))}")
else:
    print('Males left: none')
if females:
    females = list(females)
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print('Females left: none')
