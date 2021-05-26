numbers = [int(el) for el in input().split(" ")]
command = input()

while not command == "Mort":
    command_data = command.split()
    if command_data[0] == "Add":
        numbers.append(int(command_data[1]))
    elif command_data[0] == "Remove":
        if int(command_data[1]) in numbers:
            numbers.remove(int(command_data[1]))
    elif command_data[0] == "Replace":
        for index in range(len(numbers)):
            if numbers[index] == int(command_data[1]):
                numbers[index] = int(command_data[2])
                break
    elif command_data[0] == "Collapse":
        for n in numbers:
            if n < int(command_data[1]):
                numbers.remove(n)
    command = input()
numbers = [str(el) for el in numbers]
print(" ".join(numbers))
