expression = input()
s = []
for i in range(len(expression)):
    ch = expression[i]
    if ch == "(":
        s.append(i)
    elif ch == ")":
        p = s.pop()
        print(expression[p:i + 1])
