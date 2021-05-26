people_first_employee = int(input())
people_second_employee = int(input())
people_third_employee = int(input())
total_people = int(input())
hour = 0
total_hour = 0
# no_customers = False

people_per_hour = people_first_employee + people_second_employee + people_third_employee

# if total_people == 0:
#     no_customers = True

while total_people > 0:
    total_people -= people_per_hour
    hour += 1
    if hour >= 3:
        total_hour += hour + 1
        hour = 0
else:
    if hour < 3:
        total_hour = total_hour + hour
    print(f"Time needed: {total_hour}h.")
