current_version = input().split(".")
next_version = int("".join(current_version)) + 1
result = list(str(next_version))
print(".".join(result))
