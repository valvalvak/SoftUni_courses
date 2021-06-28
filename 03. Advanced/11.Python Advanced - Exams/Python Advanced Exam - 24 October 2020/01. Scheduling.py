# def get_count_of_all_tasks_to_target_heap(tasks, target):
#     heap = []
#     for (idx, task) in enumerate(tasks):
#         heappush(heap, (task, idx))
#
#     cycles = 0
#
#     while True:
#         (task, idx) = heappop(heap)
#         cycles += task
#         if idx == target:
#             break
#
#     return cycles

def get_list_of_jobs_cycles(_input_):
    task_list = [int(x) for x in _input_.split(", ")]
    return task_list


def get_count_of_all_tasks_to_target_sorted(tasks, target):
    sorted_tasks = sorted([(val, idx) for (idx, val) in enumerate(tasks)])

    cycles = 0

    for (task, idx) in sorted_tasks:
        cycles += task
        if idx == target:
            break
    return cycles


task_que = get_list_of_jobs_cycles(input())
target_task = int(input())
print(get_count_of_all_tasks_to_target_sorted(task_que, target_task))

# print(get_count_of_all_tasks_to_target_heap(task_que, target_task))
