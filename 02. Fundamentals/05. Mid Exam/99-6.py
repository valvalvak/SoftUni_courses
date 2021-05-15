counter = 0
sequence_of_numbers = input().split(" ")


command=input().split(" ")

while not command == ["end"]:
    # first_num = int(command[0])
    # second_num = int(command[1])
    if command[0] == command[1]:
        counter = counter + 1
        middle = len(sequence_of_numbers)/2
        new_number = "-" + str(counter) + "a"
        sequence_of_numbers.insert(int(middle), new_number)
        sequence_of_numbers.insert(int(middle), new_number)

        print(f"Invalid input! Adding additional elements to the board")
    elif int(command[0]) < 0 or int(command[1])< 0:
        counter += 1
        middle = len(sequence_of_numbers) / 2
        new_number = "-" + str(counter) + "a"
        sequence_of_numbers.insert(int(middle), new_number)
        sequence_of_numbers.insert(int(middle), new_number)
        print(f"Invalid input! Adding additional elements to the board")
    elif  sequence_of_numbers[int(command[0])] == sequence_of_numbers[int(command[1])]:
        element= sequence_of_numbers[int(command[0])]
        sequence_of_numbers.remove(element)
        sequence_of_numbers.remove(element)
        counter += 1
        print(f"Congrats! You have found matching elements - {element}!")
        if sequence_of_numbers == [] :
            print(f"You have won in {counter} turns!")
            break
    elif sequence_of_numbers[int(command[0])] != sequence_of_numbers[int(command[1])]:
        counter += 1
        print("Try again!")
    command = input().split(" ")
else:
    if not sequence_of_numbers == []:
        print("Sorry you lose :(")
        for items in range(len(sequence_of_numbers)):
            print(sequence_of_numbers[items], end=" ")