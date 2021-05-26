import re

text = input()

pattern = r"(?P<day>\d{2})(?P<separator>[\.\-\/])(?P<month>[A-Z][a-z]{2})?(?P=separator)(?P<year>\d{4})"

valid_date = [obj.groupdict() for obj in re.finditer(pattern, text)]

print("\n".join([f"Day: {data['day']}, Month: {data['month']}, Year: {data['year']}" for data in valid_date]))
