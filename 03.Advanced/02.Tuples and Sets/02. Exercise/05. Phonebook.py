record = input()
phonebook = {}
names_to_print = []

while True:
    if "-" not in set(record):
        for _ in range(int(record)):
            names_to_print.append(input())
        break
    name, phone = record.split("-")
    phonebook[name] = phone
    record = input()

for name in tuple(names_to_print):
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook[name]}")
