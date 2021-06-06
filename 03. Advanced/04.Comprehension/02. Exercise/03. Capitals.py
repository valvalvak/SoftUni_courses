def read_input():
    country = [x for x in input().split(", ")]
    capital = [x for x in input().split(", ")]
    return country, capital


def to_do_task():
    country, capital = read_input()
    result = [x for x in zip(country, capital)]
    return result


def print_solution():
    solution = to_do_task()
    for country, capital in solution:
        print(f"{country} -> {capital}")


print_solution()
