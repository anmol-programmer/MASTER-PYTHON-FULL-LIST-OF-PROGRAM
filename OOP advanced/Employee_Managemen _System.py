class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
emp1 = Employee("Satyam", 50000)
emp1.display_salary()
