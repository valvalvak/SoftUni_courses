def read_input():
    return [int(x) for x in input().split(", ")]


def to_do_task():
    task_job = read_input()
    dict = {
        "Positive": [], "Negative": [], "Even": [], "Odd": [],
    }
    [dict["Positive"].append(x) for x in task_job if x >= 0]
    [dict["Negative"].append(x) for x in task_job if x < 0]
    [dict["Even"].append(x) for x in task_job if x % 2 == 0]
    [dict["Odd"].append(x) for x in task_job if not x % 2 == 0]
    return dict


def print_solution():
    solution = to_do_task()
    for key, val in solution.items():
        print(f"{key}: {', '.join([str(x) for x in val])}")


print_solution()
