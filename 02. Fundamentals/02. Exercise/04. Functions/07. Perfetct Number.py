def perfect_number(digit):
    sum1 = 0
    for i in range(1, digit):
        if digit % i == 0:
            sum1 = sum1 + i
    if sum1 == digit:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number(number))
