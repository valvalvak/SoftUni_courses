def get_list_of_jobs_cycles(task_jobs):
    return [int(x) for x in task_jobs.split(", ")]


def get_idex_of_aimed_task_sort(value):
    while True:
        try:
            aimed_task_job = int(value)
            return aimed_task_job
        except ValueError:
            print(f"Must type intiger:{get_idex_of_aimed_task_sort(input())}")


def count_cycles(tasks, aimed_task):
    counter = 0
    pass


tasks_q = get_list_of_jobs_cycles(input())
aimed_task = get_idex_of_aimed_task_sort(input())
