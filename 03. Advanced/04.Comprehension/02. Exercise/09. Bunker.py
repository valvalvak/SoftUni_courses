categories = input().split(", ")
rows = int(input())

bunker = {category: [] for category in categories}

for _ in range(rows):
    category, item_name, quantity_quality = input().split(" - ")
    quantity, quality = quantity_quality.split(";")
    quantity, quality = quantity.split(":")[1], quality.split(":")[1]
    quantity, quality = int(quantity), int(quality)

    bunker[category].append({"Name": item_name, "Quality": quality, "Quantity": quantity})

total_items = sum([item["Quantity"] for items in bunker.values() for item in items])
average_quality = sum([item["Quality"] for items in bunker.values() for item in items])
average_quality /= len(categories)

print(f"Count of items: {total_items}")
print(f"Average quality: {average_quality:.2f}")

print(
    '\n'.join(
        f"{category} -> {', '.join(item['Name'] for item in bunker[category])}"
        for category in categories
    )
)
