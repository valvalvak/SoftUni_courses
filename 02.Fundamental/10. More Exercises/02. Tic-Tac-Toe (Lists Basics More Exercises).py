line_one = [int(x) for x in input().split(" ")]
line_two = [int(x) for x in input().split(" ")]
line_three = [int(x) for x in input().split(" ")]

player_one = False
player_two = False
draw = False

if line_one.count(1) == 3 or line_two.count(1) == 3 or line_three.count(1) == 3:
    player_one = True
if line_one.count(2) == 3 or line_two.count(2) == 3 or line_three.count(2) == 3:
    player_two = True

for num_1 in range(3):
    for num_2 in range(3):
        for num_3 in range(3):
            if num_1 == num_2 == num_3:
                if line_one[num_1] == line_two[num_2] == line_three[num_3]:
                    if line_one[num_1] == 1:
                        player_one = True
                    elif line_one[num_1] == 2:
                        player_two = True
            elif num_1 == 0 and num_2 == 1 and num_3 == 3:
                if line_one[num_1] == line_two[num_2] == line_three[num_3]:
                    if line_one[num_1] == 1:
                        player_one = True
                    elif line_one[num_1] == 2:
                        player_two = True
            elif num_1 == 2 and num_2 == 1 and num_3 == 0:
                if line_one[num_1] == line_two[num_2] == line_three[num_3]:
                    if line_one[num_1] == 1:
                        player_one = True
                    elif line_one[num_1] == 2:
                        player_two = True
if player_one:
    print("First player won")
elif player_two:
    print("Second player won")
else:
    print("Draw!")
