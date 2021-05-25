from collections import deque

gas_stations = int(input())
queue = deque()

for i in range(gas_stations):
    if i > 1000001:
        break
    fuel, distance = input().split()
    if 1 <= int(fuel) <= 10 ** 8 and 1 <= int(distance) <= 10 ** 8:
        queue.append(int(fuel))
        queue.append(int(distance))

tank = 0
circle_index = 0
negative_circle_counter = 0
index = deque()

while True:
    fuel = queue[0]
    distance = queue[1]
    if tank + fuel >= distance:
        tank += fuel - distance
        index.append(circle_index)
        negative_circle_counter = 0
    else:
        index = deque()
        tank = 0
        negative_circle_counter += 1
    if negative_circle_counter >= len(queue):
        break
    elif len(index) >= len(queue):
        break
    circle_index += 1
    queue.rotate(-2)

if index:
    print(index.popleft())
