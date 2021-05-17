from collections import deque

quantity = int(input())
orders = list(map(int, input().split(" ")))

que = deque()

for order in orders:
    que.append(order)

break_counter = 0

while True:
    if quantity <= 0 or len(que) <= 0:
        break
    current_order = que.popleft()
    if current_order < quantity:
        break_counter -= 1
        if current_order == max(orders):
            print(current_order)
        quantity -= current_order
    else:
        break_counter += 1
        que.append(current_order)
    if break_counter > len(que):
        break
if que:
    print(f"Orders left: {' '.join(map(str, que))}")
else:
    print("Orders complete")
