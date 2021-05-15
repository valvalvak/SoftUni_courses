email = input()
command = input()
asc = []
while not command == "Complete":
    command = command.split()
    if command[0] == "Make":
        if command[1] == "Upper":
            for ch in email:
                old = ch
                if ch.isalpha():
                    ch = ch.upper()
                    email = email.replace(old, ch)
            print(email)
        elif command[1] == "Lower":
            for ch in email:
                old = ch
                if ch.isalpha():
                    ch = ch.lower()
                    email = email.replace(old, ch)
            print(email)
    elif command[0] == "GetDomain":
        count = int(command[1])
        ind = len(email) - count
        second = email[ind:]
        print(second)
    elif command[0] == "GetUsername":
        if "@" in email:
            ind = email.index("@")
            res = email[:ind]
            print(res)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif command[0] == "Replace":
        char = command[1]
        email = email.replace(char, "-")
        print(email)
    elif command[0] == "Encrypt":
        for ch in email:
            ch = ord(ch)
            asc.append(str(ch))
        print(" ".join(asc))

    command = input()

