path = input().split("\\")
file = path[-1]
name, extension = file.split(".")
print(f"File name: {name}\n"
      f"File extension: {extension}")
