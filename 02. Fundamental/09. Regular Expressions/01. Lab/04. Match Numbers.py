import re

regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

text = input()

result = [obj.group() for obj in re.finditer(regex, text)]

print(*result)
