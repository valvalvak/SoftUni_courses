happy_year = int(input())
happy_year += 1
while not len(set(str(happy_year))) == len(str(happy_year)):
    happy_year += 1
print(happy_year)
