username = input()

data = input()

while data != "Sign up":
    data = data.split()
    command = data[0]
    if command == "Case":
        upper_lower = data[1]
        if upper_lower == "upper":
            username = username.upper()
            print(username)
        elif upper_lower == "lower":
            username = username.lower()
            print(username)
    elif command == "Cut":
        substring = data[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = data[1]
        username = username.replace(char, '*')
        print(username)
    elif command == "Check":
        char = data[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
    elif command == "Reverse":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            first_part = username[:start_index]
            second_part = username[end_index + 1:]
            rev_part = username[start_index:end_index + 1]
            rev_part = rev_part[::-1]
            print(rev_part)
    data = input()