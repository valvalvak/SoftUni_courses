import re

text = input()
regex = r"\d+"
result = []

while text:
    nums = re.findall(regex, text)
    result.extend(nums)
    text = input()
print(*result)