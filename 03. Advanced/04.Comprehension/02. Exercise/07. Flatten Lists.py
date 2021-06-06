"""
==========================================================================================
not working (75/100), and do not know why?! doesn't work with "reverse()" and/or reversed()
==========================================================================================
def read_input():
    raw_input = reversed(input().split("|"))
    result = [[x for x in row if x.isdigit() and int(x) >= 0] for row in raw_input]
    return result


def to_do_task():
    result = read_input()
    "result.reverse()"
    return result


def print_issue():
    issue = to_do_task()
    print(' '.join(' '.join([x for x in row]) for row in issue))


print_issue()

"""

"""
working just fine: 100/100
ok, but why?
"""
input_str = input().split("|")[::-1]

matrix = [x.split() for x in input_str]

flatten_list = [j for i in matrix for j in i]

print(" ".join(flatten_list))
