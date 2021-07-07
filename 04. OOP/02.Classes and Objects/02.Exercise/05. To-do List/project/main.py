from project.section import Section
from project.task import Task

if __name__ == '__main__':
    task = Task("Make bed", "27/05/2020")
    print(task.change_name("Go to University"))
    print(task.change_due_date("28.05.2020"))
    task.add_comment("[finish my homework, pay the bills]")
    task.add_comment("[finish my homework, pay the bills]")
    task.add_comment("[finish my homework, pay the bills]")
    print(task.edit_comment(0, "[finish my homework]"))
    print(task.edit_comment(1, "[pay the bills]"))
    print(task.edit_comment(2, "[finish my homework]"))
    print(task.details())
    section = Section("Daily tasks")
    print(section.add_task(task))
    second_task = Task("Make bed", "27/05/2020")
    section.add_task(second_task)
    print(section.clean_section)
    print(section.view_section())

# [print({key}:{value} for key, value in dict.items()]
