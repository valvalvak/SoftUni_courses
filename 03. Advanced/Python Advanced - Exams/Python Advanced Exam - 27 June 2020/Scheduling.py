from collections import deque

def get_list_of_jobs_cycles():
    jobs_list = [int(x) for x in input().split(", ")]
    return jobs_list

def get_count_of_all_tasks_to_target(tasks, target):
    clock_cycle = 0
    priority_task = min(tasks)
    current_task = tasks[0]
    
    while tasks:
        if current_task == priority_task == target:
            return clock_cycle
        else:
            clock_cycle +=1
            if not current_task == priority_task:
                tasks.rotate(-1)
            else:
                tasks.popleft()
 
        

task_que = deque(get_list_of_jobs_cycles())
target_task = int(input())
print(get_count_of_all_tasks_to_target(task_que, task_que[target_task]))