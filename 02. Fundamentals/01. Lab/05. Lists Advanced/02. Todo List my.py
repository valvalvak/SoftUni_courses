command = input()
result = [0] * 10
while not command == "End":
    priority, todo = command.split("-")
    index = int(priority)
    if index <= 10:
        result.insert(index - 1, todo)
    else:
        pass
    command = input()
todo_notes = []
for el in range(len(result)):
    if not result[el] == 0:
        todo_notes.append(result[el])
print(todo_notes)
