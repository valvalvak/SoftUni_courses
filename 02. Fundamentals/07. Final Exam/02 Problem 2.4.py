import re

count = int(input())
regex = r"(.+)[>](?P<meat>(\d{3})\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})[<](\1)"
text = ""
pass_list = []
for r in range(count):
    text = input()
    current_regex = [obj.group("meat") for obj in re.finditer(regex, text)]
    if not current_regex:
        print("Try another password!")
        continue
    else:
        result = "|".join(current_regex)
        result = result.replace("|", "")
        print(f"Password: {result}")