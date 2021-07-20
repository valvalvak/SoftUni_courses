from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return "teaching..."


print(Teacher.teach())
print(Teacher.sleep())
print(Teacher.get_fired())
