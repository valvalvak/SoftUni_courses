def read_input():
    raw_input = [x for x in input().split("|")]
    result = [row.split() for row in raw_input]
    return result


def to_do_task():
    result = read_input()
    result.reverse()
    return result


def print_issue():
    issue = to_do_task()
    print(' '.join(' '.join([x for x in row]) for row in issue if len(row) > 0))


print_issue()

#
# input_str = input().split("|")[::-1]
#
# matrix = [x.split() for x in input_str]
#
# flatten_list = [j for i in matrix for j in i]
#
# print(" ".join(flatten_list))
