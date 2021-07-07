from typing import List

from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {Task.details(new_task)} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                Task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    @property
    def clean_section(self):
        amount_of_removed_tasks = 0
        for task in self.tasks:
            if task is True:
                amount_of_removed_tasks += 1
                self.tasks.remove(task)
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        result_str = ""
        result_str += "Section " + str(self.name) + ":\n"
        for task in self.tasks:
            result_str += str(Task.details(task)) + "\n"
        return result_str
