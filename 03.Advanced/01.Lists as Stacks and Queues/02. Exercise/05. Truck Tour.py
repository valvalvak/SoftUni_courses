from collections import deque

gas_stations = int(input())
queue = deque()

for i in range(gas_stations):
    if i > 1000001:
        break
    fuel, distance = input().split()
    if 1 <= int(fuel) <= 1000000000 and 1 <= int(distance) <= 1000000000:
        queue.append(int(fuel))
        queue.append(int(distance))

tank = 0
counter = 0
index = deque()

while queue:
    if not len(queue) > abs(counter):
        break
    else:
        fuel = queue[0]
        distance = queue[1]
        difference = abs(distance - fuel)
        if fuel + tank >= distance:
            tank += difference
            index.append(counter)
        else:
            if index:
                index.popleft()
            tank = 0
    queue.rotate(-2)
    counter += 1

if index:
    print(index.popleft())
