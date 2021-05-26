factor = int(input())
count = int(input())
new_list = []
digit = 0
for _ in range(count):
    digit += factor
    new_list.append(digit)
print(new_list)
