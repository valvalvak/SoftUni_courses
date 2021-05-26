permutation = input().split(" ")
shoot_turn = int(input())
current_man = shoot_turn - 1  # index in list
death_list = []

while not len(permutation) <= 0:
    if not current_man >= len(permutation):
        current = permutation.pop(current_man)
        death_list.append(current)
        current_man += shoot_turn - 1
    else:
        current_man -= len(permutation)

print(f'[{",".join(death_list)}]')
