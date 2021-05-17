from collections import deque

quantity = int(input())
orders = list(map(int, input().split(" ")))

que = deque()

for order in orders:
    que.append(order)

while True:
    if quantity <= 0 or len(que) <= 0:
        break
    current_order = que[0]
    if current_order <= quantity:
        que.popleft()
        quantity -= current_order
    else:
        break
print(max(orders))
if que:
    print(f"Orders left: {' '.join(map(str, que))}")
else:
    print("Orders complete")
