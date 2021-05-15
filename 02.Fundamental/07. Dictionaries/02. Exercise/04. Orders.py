order = input()

products = {}

while not order == "buy":
    name, price, quantity = order.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        products[name]["quantity"] += quantity
        products[name]["price"] = price

    order = input()
for key, value in products.items():
    print(f"{key} -> {value['price'] * value['quantity']:.2f}")
