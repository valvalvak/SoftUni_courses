VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(x.upper() for x in VOWELS)
# [VOWELS.add(x.upper()) for x in list(VOWELS)]

text = input()
result = [ch for ch in text if ch not in VOWELS]
print(''.join(result))

# vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
# print(''.join([x for x in input() if x not in vowels]))
