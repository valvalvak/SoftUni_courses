def read_word():
    result_as_list = [x for x in input().split(" ")]
    return result_as_list


def to_do_case():
    raw_case = read_word()
    solution_result = [x for x in raw_case if len(x) % 2 == 0]
    return solution_result


print('\n'.join([x for x in to_do_case()]))
