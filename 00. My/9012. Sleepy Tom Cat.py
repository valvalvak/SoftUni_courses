holidays = int(input())
tom_norm_per_year = 30000
workdays_multiply = 63
holidays_multiply = 127
workdays = 365 - holidays
day_to_minutes = 24 * 60
calculated_time_sum = int(workdays * workdays_multiply + holidays * holidays_multiply)
difference = abs(tom_norm_per_year - calculated_time_sum)
if calculated_time_sum >= tom_norm_per_year:
    print(f"Tom will run away")
    print(f"{difference // 60} hours and {difference % 60} minutes less for play")
else:
    print("Tom sleeps well")
    print(f"{difference // 60} hours and {difference % 60} minutes less for play")
# did you mean "More for Tom to rest???"
# print(a * b)
# for n in range(len(123)):
#     test = 0
