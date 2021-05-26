race_list = [int(x) for x in input().split()]

left_list = race_list[:len(race_list) // 2]
right_list = race_list[(len(race_list) + 1) // 2:]
right_list.reverse()
mid_one = race_list[len(race_list) // 2]
left_racer = 0
right_racer = 0
for i in range(len(left_list)):
    if not left_list[i] == 0:
        left_racer += left_list[i]
    else:
        left_racer *= 0.8
for i in range(len(right_list)):
    if not right_list[i] == 0:
        right_racer += right_list[i]
    else:
        right_racer *= 0.8
if left_racer < right_racer:
    print(f"The winner is left with total time: {left_racer:.1f}")
elif right_racer < left_racer:
    print(f"The winner is left with total time: {right_racer:.1f}")
