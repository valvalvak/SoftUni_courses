electrons = int(input())
position = 0
shell_list = []
while not electrons <= 0:
    position += 1
    formula = 2 * pow(position, 2)
    if formula < electrons:
        shell_list.append(formula)
    else:
        shell_list.append(electrons)
    electrons -= formula
print(shell_list)
