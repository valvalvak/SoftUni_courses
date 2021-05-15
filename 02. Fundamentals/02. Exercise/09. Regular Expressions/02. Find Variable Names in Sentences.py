import re

text = input()

regex = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

result = [obj.group() for obj in re.finditer(regex, text)]

print(",".join(result))