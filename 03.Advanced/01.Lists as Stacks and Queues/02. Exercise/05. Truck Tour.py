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
while_break_case = len(queue)

while queue:
    counter += 1
    fuel = queue.popleft()
    distance = queue.popleft()
    difference = distance - fuel
    if fuel >= distance + tank:
        tank += difference
        index.append(counter - 1)
        continue
    else:
        queue.append(fuel)
        queue.append(distance)
    if counter >= while_break_case:
        break
print(index.popleft())
