rows = int(input())
wall = []
free = " "
for i in range(rows):
    wall.append(input())
    counter = wall[i].count("#")

    if counter < len(wall[i]):
        if "k" in wall[i]:
            if free in wall[i]:
                print(f"K!@index:{wall[i].index('k')} free slots:{wall[i].count(free)}@index:{wall[i].index(free)}")
            else:
                print(f"K! but ain't a way")
    else:
        print("No way")
print(wall)
