from collections import deque


def define_delivery_case(cupcake_flavours, rest):
    _, *rest_que = rest
    rest_que = deque(rest_que)
    for el in rest_que:
        if not el == "sell" or not type(el) == int:
            cupcake_flavours.append(el)
    return cupcake_flavours


def define_sell_case(cupcake_flavours, rest):
    _, *rest_que = rest
    rest_que = deque(rest_que)

    if not rest_que:
        cupcake_flavours.popleft()
        return cupcake_flavours

    while rest_que:
        curent_el = rest_que.popleft()
        try:
            value = int(curent_el)
            for _ in range(value):
                cupcake_flavours.popleft()
            continue
        except ValueError:
            pass
        if not curent_el == "delivery":
            try:
                while curent_el in cupcake_flavours:
                    cupcake_flavours.remove(curent_el)
            except ValueError:
                continue
    return cupcake_flavours


def stock_availability(*args):
    cupcake_flavours, *rest = args
    cupcake_flavours = deque(cupcake_flavours)
    for el in rest:
        if el == "delivery":
            cupcake_flavours = define_delivery_case(cupcake_flavours, rest)
        elif el == "sell":
            cupcake_flavours = define_sell_case(cupcake_flavours, rest)
    return list(cupcake_flavours)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
