fire_size_cells = input().split("#")
water = int(input())

low_fire_range = range(1, 51)
medium_fire_range = range(51, 81)
high_fire_range = range(81, 126)

fire_out = 0
effort = 0

print("Cells:")

for i in range(len(fire_size_cells)):

    fire_type, fire_size = fire_size_cells[i].split(" = ")
    fire_size = int(fire_size)

    if fire_type == "Low":
        if fire_size in low_fire_range:
            if water >= fire_size:
                water -= fire_size
                fire_out += fire_size
                effort += fire_size * 0.25
                print(f" - {fire_size}")
            else:
                continue
    if fire_type == "Medium":
        if fire_size in medium_fire_range:
            if water >= fire_size:
                water -= fire_size
                fire_out += fire_size
                effort += fire_size * 0.25
                print(f" - {fire_size}")
            else:
                continue
    if fire_type == "High":
        if fire_size in high_fire_range:
            if water >= fire_size:
                water -= fire_size
                fire_out += fire_size
                effort += fire_size * 0.25
                print(f" - {fire_size}")
            else:
                continue

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_out}")
