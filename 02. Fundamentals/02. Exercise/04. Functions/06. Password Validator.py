def password_chek(word):
    is_valid = True
    if not len(word) >= 6 and len(word) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not word.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    if sum(list(map(lambda x: 1 if x.isdigit() else 0, set(word)))) < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        return "Password is valid"
    else:
        exit(0)


password = input()

print(password_chek(password))
