working_row = input()

# working_row = "SoftUni rocks"

for el in sorted(set(working_row)):
    print(f"{el}: {working_row.count(el)} time/s")
