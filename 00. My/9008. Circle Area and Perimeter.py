import math

radius = float(input())
calculated_area = math.pi * math.pow(radius, 2)
calculated_perimeter = math.pi * (radius * 2)
print(f"{calculated_area:.2f}\n{calculated_perimeter:.2f}")
