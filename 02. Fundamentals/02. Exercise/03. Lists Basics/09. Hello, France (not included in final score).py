# max price not to by over
CLOTHES = 50.00
SHOES = 35.00
ACCESSORIES = 20.50
# needed for the trip to France
FRANCE = 150

items_list = input().split("|")
budget = float(input())

selling_list = []
profit = 0


for item in range(len(items_list)):
    item_type, item_price = items_list[item].split("->")
    item_price = float(item_price)
    if item_price > budget:
        continue
    else:
        if item_type == "Clothes" and item_price <= CLOTHES:
            selling_list.append(item_price*1.4)
            profit += item_price * 0.4
            budget -= item_price
        elif item_type == "Shoes" and item_price <= SHOES:
            selling_list.append(item_price*1.4)
            profit += item_price * 0.4
            budget -= item_price
        elif item_type == "Accessories" and item_price <= ACCESSORIES:
            selling_list.append(item_price*1.4)
            profit += item_price * 0.4
            budget -= item_price
for new_price in selling_list:
    print(f"{new_price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if sum(selling_list)+profit >= FRANCE:
    print("Hello, France!")
else:
    print("Time to go.")