txt = input()
word = input()
while txt in word:
    word = word.replace(txt, "")
print(word)
