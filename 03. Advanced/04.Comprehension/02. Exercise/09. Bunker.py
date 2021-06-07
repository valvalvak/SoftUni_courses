all_item_categories = input().split(", ")
n = int(input())

bunker = {}

for _ in range(n):
    # "{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}"
    # food - pizza - quantity:10;quality:5
    # water - mineral - quantity:5;quality:10
    # materials - wood - quantity:2;quality:5
    # metal - copper - quantity:3;quality:10
    # food - burgers - quantity:5;quality:2 
    category, item, quantity_quality = input().split("-")
    item_quantity = quantity_quality.split(";")[1]
    item_quality = quantity_quality.split(";")[1]
    

