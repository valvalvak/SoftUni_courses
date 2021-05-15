text = input()
res = ":"
for i in range(len(text)):
    if text[i] == res:
        symbol = str(text[i+1])
        print(res+symbol)
