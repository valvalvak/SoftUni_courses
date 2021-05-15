usernames = input().split(", ")

valid_characters = ["-", "_"]
isValid = False
for name in usernames:
    if not (3 <= len(name) <= 16):
        continue
    else:
        for content in name:
            if content.isalpha():
                isValid = True
                continue
            elif content.isdigit():
                isValid = True
                continue
            elif content in valid_characters:
                isValid = True
                continue
            else:
                isValid = False
                break
    if isValid:
        print(name)
