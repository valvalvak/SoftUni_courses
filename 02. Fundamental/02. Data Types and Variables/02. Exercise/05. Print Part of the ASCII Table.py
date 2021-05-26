start = int(input())
end = int(input())

for index in range(start, end + 1):
    char = chr(index)
    print(f"{char}", end=" ")
