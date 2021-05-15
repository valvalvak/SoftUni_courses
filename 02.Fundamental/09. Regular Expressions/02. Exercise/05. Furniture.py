import re

regex = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"

furniture_list = []
total_cost = 0
text = input()
while not text == "Purchase":
    mach = re.match(regex, text)
    if mach:
        data = mach.groupdict()
        furniture_list.append(data['name'])
        total_cost += float(data['price']) * int(data['quantity'])
    text = input()

print(f"Bought furniture:")
for el in furniture_list:
    print(f"{el}")
print(f"Total money spend: {total_cost:.2f}")
