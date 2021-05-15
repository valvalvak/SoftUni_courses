username = input()
command = input()

while not command == "Sign up":
    data = command.split()
    if data[0] == "Case":
        task = data[1]
        if task == "lower":
            username = username.lower()
            print(username)
        elif task == "upper":
            username = username.upper()
            print(username)
    elif data[0] == "Reverse":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            result = username[start_index:end_index + 1]
            result = result[::-1]
            print(result)
    elif data[0] == "Cut":
        substring = data[1]
        if substring not in username:
            print(f"The word {username} doesn't contain {substring}.")
        else:
            username = username.replace(substring, "")
            print(username)
    elif data[0] == "Replace":
        char = data[1]
        username = username.replace(char, "*")
        print(username)
    elif data[0] == "Check":
        char = data[1]
        if char not in username:
            print(f"Your username must contain {char}.")
        else:
            print("Valid")
    command = input()
