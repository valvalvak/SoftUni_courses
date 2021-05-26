import re

pattern = r"(\||#)(?P<name>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9][0-9]{0,3}|10000)\1"

text = input()
food_data = [match for match in re.finditer(pattern, text)]

days = sum([int(food['calories']) for food in food_data]) // 2000

print(f"You have food to last you for: {days} days!")
for food in food_data:
    print(f"Item: {food['name']}, Best before: {food['date']}, Nutrition: {food['calories']}")

# TODO test comment
