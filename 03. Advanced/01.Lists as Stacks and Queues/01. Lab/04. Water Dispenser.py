from collections import deque

dispenser_amount = int(input())

people_queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    people_queue.append(command)

while True:
    command = input()
    if command == "End":
        print(f"{dispenser_amount} liters left")
        break
    if command.startswith("refill"):
        refill, litres = command.split()
        litres = int(litres)
        dispenser_amount += litres
    else:
        person = people_queue.popleft()
        person_litres = int(command)
        if person_litres <= dispenser_amount:
            print(f"{person} got water")
            dispenser_amount -= person_litres
        else:
            print(f"{person} must wait")
