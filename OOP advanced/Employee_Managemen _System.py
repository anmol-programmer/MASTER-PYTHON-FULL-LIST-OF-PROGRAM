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


def info():
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
n=int(input("do you want to know about the program just click 1 otherwise press any number:"))
if n==1:
    info(info.__doc__)
dev_name=input("enter the developer name:")
dev_base_salary=int(input("enter the base salary of the developer:"))
dev_bouns=int(input("enter the bouns of the developer:"))
print("\n")
mgr_name=input("enter the manager  name:")
mgr_base_salary=int(input("enter the base salary of the manager:"))
mgr_bouns=int(input("enter the bouns of the manager:"))
mgr_allowance=int(input("enter the allowance of the manager:"))

dev = Developer(dev_name, dev_base_salary, dev_bouns)
mgr = Manager(mgr_name, mgr_base_salary, mgr_bouns, mgr_allowance)
print(f"Developer Salary: {dev.calculate_salary()}")
print(f"Manager Salary: {mgr.calculate_salary()}")

