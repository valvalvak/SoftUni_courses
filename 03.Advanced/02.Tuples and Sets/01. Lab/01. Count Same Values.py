values = tuple(input().split(" "))

counter_dictionary = {}

for el in values:

    if el not in counter_dictionary:
        counter_dictionary[el] = 0
    counter_dictionary[el] += 1

for num, count in counter_dictionary.items():
    print(f"{float(num)} - {count} times")
