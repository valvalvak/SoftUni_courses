class Task:
    comments: List = []
    completed: bool = False

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date

    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    @staticmethod
    def add_comment(comment: str):
        Task.comments.append(comment)

    @staticmethod
    def edit_comment(comment_number: int, new_comment: str):
        if not 0 <= comment_number < len(Task.comments):
            return "Cannot find comment."
        Task.comments[comment_number] = new_comment
        comments_result = ", ".join(Task.comments)
        return comments_result

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


if __name__ == '__main__':
    task = Task("Make bed", "27/05/2020")
    print(task.change_name("Go to University"))
    print(task.change_due_date("28.05.2020"))
    task.add_comment("Don't forget laptop")
    print(task.edit_comment(0, "Don't forget laptop and notebook"))
    print(task.details())
    section = Section("Daily tasks")
    print(section.add_task(task))
    second_task = Task("Make bed", "27/05/2020")
    section.add_task(second_task)
    print(section.clean_section())
    print(section.view_section())
