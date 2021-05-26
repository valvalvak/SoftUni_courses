tmp = input()
stock = {}
while not tmp == "statistics":
    key, value = tmp.split(":")
    if key not in stock:
        stock[key] = int(value)
    else:
        stock[key] += int(value)
    tmp = input()
print(f"Products in stock:")
for (key, value) in stock.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")
