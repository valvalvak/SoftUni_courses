import re

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

text = input()

matches = [obj.group() for obj in re.finditer(pattern, text)]

print(", ".join(matches))
