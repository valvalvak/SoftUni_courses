class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = int(id)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.salary = int(salary)

    def get_full_name(self):
        """get_full_name() - returns "{first_name} {last_name}"""
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        """get_annual_salary() - returns the total salary for 12 months"""
        self.salary *= 12
        return self.salary

    def raise_salary(self, rise_amout):
        """raise_salary(amount) - increases the salary by the given amount and returns the new salary"""
        self.salary += rise_amout
        return self.salary


employee = Employee(1, "1", "2", 1)
print(employee.id)
print(employee.get_full_name())
print(employee.raise_salary(199))
print(employee.get_annual_salary())
