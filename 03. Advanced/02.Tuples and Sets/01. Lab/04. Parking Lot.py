def read_lines_list(inputs):
    lines = []
    for _ in range(inputs):
        lines.append(input())
    return lines


parking_set_lines = read_lines_list(int(input()))

parking_occupancy = set()

for el in parking_set_lines:
    check_in_out, plate = el.split(", ")
    if check_in_out == "IN":
        parking_occupancy.add(plate)
    elif check_in_out == "OUT":
        parking_occupancy.discard(plate)
if not parking_occupancy:
    print("Parking Lot is Empty")
else:
    for el in parking_occupancy:
        print(el)
