string = input().split()
new_string = []
for i in range(len(string)):
    digit = int(string[i]) * -1
    new_string.append(digit)
print(new_string)
