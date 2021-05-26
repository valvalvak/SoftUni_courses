command = input().split()
list_range = int(command[0])
wagons = []
for _ in range(list_range):
    wagons.append(0)
while not command[0] == "End":
    if command[0] == "add":
        wagons[-1] += int(command[-1])
    elif command[0] == "insert":
        index = int(command[1])
        wagons[index] += int(command[2])
    elif command[0] == "leave":
        index = int(command[1])
        wagons[index] -= int(command[2])
    command = input().split()
wagons = [int(x) for x in wagons]
print(wagons)
