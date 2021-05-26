word1, word2 = input().split(" ")

if not len(word1) > len(word2):
    multiply = len(word1)
else:
    multiply = len(word2)

res = 0

for ch in range(multiply):
    res += ord(word1[ch]) * ord(word2[ch])

res += sum(ord(x) for x in word1[multiply::]) + sum(ord(x) for x in word2[multiply::])

print(res)
