values = input().split(" ")
counter_dictionary = {}
for el in values:
    if not counter_dictionary[el] in counter_dictionary:
        counter_dictionary[el] = 1
    counter_dictionary[el] += 1
print(counter_dictionary)
