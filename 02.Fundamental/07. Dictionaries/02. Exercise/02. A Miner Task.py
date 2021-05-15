command = input()
resources = {}
while not command == "stop":
    quantity = int(input())
    if command in resources:
        resources[command] += quantity
    else:
        resources[command] = quantity
    command = input()
for res in resources:
    print(f"{res} -> {resources[res]}")
