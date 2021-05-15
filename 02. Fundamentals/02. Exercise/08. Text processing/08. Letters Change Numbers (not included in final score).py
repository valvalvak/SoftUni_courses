def current_case(string):
    num = ""
    for el in string:
        if not el.isnumeric():
            continue
        else:
            num += el
    return int(num)


result = []

objective = input().split()
for case in objective:
    current_num = current_case(case)
    if case[0].isupper():
        char_as_num = (ord(case[0]) - 64)
        current_num /= char_as_num
    elif case[0].islower():
        char_as_num = (ord(case[0]) - 96)
        current_num *= char_as_num
    if case[-1].isupper():
        char_as_num = (ord(case[-1]) - 64)
        current_num -= char_as_num
    elif case[-1].islower():
        char_as_num = (ord(case[-1]) - 96)
        current_num += char_as_num
    result.append(current_num)

total_sum = 0

for n in result:
    total_sum += n

print(f"{total_sum:.2f}")
