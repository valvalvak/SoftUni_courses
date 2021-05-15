text = input()
res = ""
for i in text:
    res += chr(ord(i) + 3)
print(res)
