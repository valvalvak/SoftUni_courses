import re

message = input()

# regex = r"(|[a-zA-Z0-9]+?(\.|-|_))?[a-zA-Z0-9]+?@[a-zA-Z0-9]+(((\.|-)[a-zA-Z0-9]+)+|)"

regex = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

result = [obj.group() for obj in re.finditer(regex, message)]

print(*result, sep="\n")
