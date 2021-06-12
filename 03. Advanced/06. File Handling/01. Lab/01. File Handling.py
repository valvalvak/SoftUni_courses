# file = open('02_example.txt', 'r')

# file = open('invalid.txt', 'r')

# try:
#     file = open('invalid.txt', 'r')  # FileNotFoundError
# except FileNotFoundError:
#     print("File not found or path is incorrect")
# finally:
#     print("exit")

# try:
#     text_file = open('02_example.txt', 'r')
#     print("File found")
# except FileNotFoundError:
#     print("File not found")

# file = open("asd.txt")  # 'Hello, SoftUni!'
# print(file.read(2))     # 'He'
# print(file.read(2))     # 'll'
# print(file.read(2))     # 'o,'
# print(file.read())      # ' SoftUni!'

# file = open("02_example.txt")  # 'Hello, SoftUni!'
# print(file.readline(5))  # 'Hello'
# print(file.readline(5))  # ' ,Sof'
# print(file.readline(5))  # 'tUni!'
# print(file.readline())   # '' Goes to the new line
# print(file.readline(5))  # 'Secon' Print second line

# file = open("text.txt")
# print(file.readlines())  # ['Every\n', 'Word\n', 'is\n', 'line']

# file = open("text.txt")
# lines = file.readlines()
# [print(line, end="") for line in lines]

# file = open("python.txt", 'r')

# for line in file:
#     print(line, end="") # print every line in a new line

# numbers_file = open('numbers.txt', 'r')
# numbers_sum = 0
# for number in numbers_file:
#     numbers_sum += int(number)
# print(numbers_sum)

# file = open('python.txt', 'w') # Creates or open the file 

# file.write("This is the write command.\n")
# file.write("It allows us to write in a particular file")
# file.close()

# file = open('python.txt', 'a')
# file.write("This is the write command.\n")
# file.write("It allows us to write in a particular file")
# file.close()

# file = open('python.txt', 'a')
# lines = ["Write ", "in ", "file"]
# file.writelines(lines)  # Write multiple strings
# file.close()

# with open("file.txt", "w") as f:
#     f.write("Hello World!!!")

# created_file = open('my_first_file.txt', 'w')
# created_file.write('I just created my first file!')

# import os

# os.remove("python.txt")
# os.remove("D:\\text.txt")  # Can use full path

# import os

# file_path = "text.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)

# import os
# try:
#     os.remove('my_first_file.txt')
# except FileNotFoundError:
#     print("File already deleted!")

