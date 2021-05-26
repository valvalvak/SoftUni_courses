substrings = input().split(", ")
words = input().split(", ")

find_substrings = []

for subs_string in substrings:
    for word in words:
        if subs_string in word:
            find_substrings.append(subs_string)

print(list(sorted(set(find_substrings), key=find_substrings.index)))
