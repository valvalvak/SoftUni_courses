numbers_dictionary = {}

key = input()
while not key == "Search":
    try:
        number = int(input())
        numbers_dictionary[key] = number
    except ValueError:
        print("The variable number must be an integer")
    key = input()


while True:
    key = input()
    if key == "Remove":
        break
    try:
        print(numbers_dictionary[key])
    except KeyError:
        print("Number does not exist in dictionary")

while True:
    key = input()
    if key == "End":
        break
    try:
        del numbers_dictionary[key]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
