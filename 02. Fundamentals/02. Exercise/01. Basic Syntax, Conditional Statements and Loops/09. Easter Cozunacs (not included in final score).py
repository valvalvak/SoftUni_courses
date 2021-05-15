budget = float(input())
flour_price = float(input())

egg_pack_price = flour_price * 0.75
liter_milk_price = flour_price * 1.25
cozunac_milk_price = liter_milk_price * 0.25

cozunac_price = egg_pack_price + flour_price + cozunac_milk_price

cozunacs = 0
color_eggs = 0


while not budget <= cozunac_price:
    cozunacs += 1
    budget -= cozunac_price
    color_eggs += 3
    if cozunacs % 3 == 0:
        color_eggs -= cozunacs - 2


print(f"You made {int(cozunacs)} cozonacs! Now you have {int(color_eggs)} eggs and {budget:.2f}BGN left.")