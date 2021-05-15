text = input()  # aaaaabbbbbcdddeeeedssaa
res = ""
last = ""
new = ""
for ch in text:
    new = ch
    if not new == last:
        res += new
        last = new
print(res)  # abcdedsa
