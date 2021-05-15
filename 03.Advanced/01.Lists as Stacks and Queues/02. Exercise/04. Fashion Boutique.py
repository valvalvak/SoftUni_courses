box = list(map(int, input().split()))
capacity = int(input())

racks_counter = 1
current_capacity = capacity

while len(box) > 0:
    current_clothes_value = box.pop()
    if current_capacity > current_clothes_value:
        current_capacity -= current_clothes_value
    else:
        racks_counter += 1
        current_capacity = capacity
        current_capacity -= current_clothes_value
print(racks_counter)
