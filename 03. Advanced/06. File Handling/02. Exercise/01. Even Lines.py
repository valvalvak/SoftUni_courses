# created_file = open('even_lines.txt', 'w')
# created_file.write(
#     "-I was quick to judge him, but it wasn't his fault."'\n'
#     "-Is this some kind of joke?! Is it?"'\n'
#     "-Quick, hide here. It is safer.")

file = open("even_lines.txt")
print(file.readlines(1))
file.close()
#
# for index, line in enumerate(file.readlines()):
#     # if not index % 2 == 0:
#     #     continue
#     print(index, line)
