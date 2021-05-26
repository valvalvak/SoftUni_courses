command = input()

staff = {}

while not command == "End":

    company, employee = command.split(" -> ")

    if company not in staff:
        staff[company] = [employee]

    elif employee not in staff[company]:
        staff[company] += [employee]

    command = input()

for company, employee in sorted(staff.items(), key=lambda x: x[0]):
    print(company)

    for emp_id in employee:
        print(f"-- {emp_id}")
