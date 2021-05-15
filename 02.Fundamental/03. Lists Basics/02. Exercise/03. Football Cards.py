players_list = input().split()

team_a = 11
team_b = 11
check_list = []

for i in range(len(set(players_list))):
    check_list.append(players_list[i])
    if any("A" in a for a in check_list):
        team_a -= 1
    if any("B" in b for b in check_list):
        team_b -= 1
    if team_a < 7 or team_b < 7:
        break
    check_list.clear()
if team_a >= 7 and team_b >= 7:
    print(f"Team A - {team_a}; Team B - {team_b}")
else:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print("Game was terminated")
