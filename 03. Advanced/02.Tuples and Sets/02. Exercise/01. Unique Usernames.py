def add_to_set(n_lines):
    set_values = set()
    for _ in range(n_lines):
        set_values.add(input())
    return set_values


def print_line(n_inputs_to_set):
    for item in n_inputs_to_set:
        print(item)


n_inputs_to_set = add_to_set(int(input()))
print_line(n_inputs_to_set)
