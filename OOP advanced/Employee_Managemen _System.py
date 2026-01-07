class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

class Developer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class Manager(Employee):
    def __init__(self, name, base_salary, bonus, allowance):
        super().__init__(name, base_salary)
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.bonus + self.allowance

dev = Developer("satyam", 50000, 10000)
mgr = Manager("anmol", 70000, 15000, 8000)

print(f"Developer Salary: {dev.calculate_salary()}")
print(f"Manager Salary: {mgr.calculate_salary()}")

"""1️⃣ Inheritance – Employee Management System

Concept: Inheritance, method overriding

Problem:
Create a base class Employee with:
name
base_salary
method calculate_salary()

Create child classes:

Developer → salary = base + bonus

Manager → salary = base + bonus + allowance

📌 Job Use: HR payroll systems"""