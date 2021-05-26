s = [x for x in input().split()]
res = ""
while s:
    res += s.pop() + " "
print(res.strip())
