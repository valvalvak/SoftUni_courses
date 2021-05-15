n = int(input())
parking = {}

for _ in range(n):
    command = input().split()
    if command[0] == "register":
        name, plate = command[1], command[2]
        if name not in parking:
            parking[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")
    if command[0] == "unregister":
        name = command[1]
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking[name]
for name, plate in parking.items():
    print(f"{name} => {plate}")
