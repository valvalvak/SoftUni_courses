command = input()
result = [0] * 10
while not command == "End":
    priority, todo = command.split("-")
    priority = int(priority) - 1
    result[priority] = todo
    command = input()
print([todo for todo in result if not todo == 0])
