nums_as_strings = input()

nums_as_ints = [int(x) for x in nums_as_strings]

nums_as_ints.sort(reverse=True)

for el in nums_as_ints:
    print(el, end="")

