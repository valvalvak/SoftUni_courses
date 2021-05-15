number = input().split(" ")

big_number = list(sorted(number, reverse=True))

print("".join(big_number))
