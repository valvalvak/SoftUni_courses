text = input()
digits = ""
letters = ""
others = ""
for character in text:
    if character.isdigit():
        digits += character
    elif character.isalpha():
        letters += character
    else:
        others += character
print(f"{digits}\n{letters}\n{others}")
