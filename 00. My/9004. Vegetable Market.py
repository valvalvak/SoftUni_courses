vegetables_bgn_price_per_kg = float(input())
fruits_bgn_price_per_kg = float(input())
all_vegetables_in_kg = int(input())
all_fruits_in_kg = int(input())
vegetables_euro_income = vegetables_bgn_price_per_kg * all_vegetables_in_kg / 1.94
fruits_euro_income = fruits_bgn_price_per_kg * all_fruits_in_kg / 1.94
total_income_in_euro = vegetables_euro_income + fruits_euro_income
print(f"{total_income_in_euro:.2f}")
