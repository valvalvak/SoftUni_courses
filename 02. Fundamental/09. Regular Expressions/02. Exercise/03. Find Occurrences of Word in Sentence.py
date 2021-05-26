import re

text = input()
word = input()

regex = rf"\b{word}\b"

result = re.findall(regex, text, re.IGNORECASE)

print(len(result))
