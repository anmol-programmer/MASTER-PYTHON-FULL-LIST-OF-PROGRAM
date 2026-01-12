"""
Title: Employee Salary Eligibility Filter
Description:
This program filters employees whose salary is greater than 50,000.
Commonly used in payroll systems, HR analytics, and bonus eligibility checks.
"""

employees = [
    {"name": "A", "salary": 45000},
    {"name": "B", "salary": 60000},
    {"name": "C", "salary": 80000}
]

def is_salary_eligible(employee):
    """
    Business Rule:
    An employee is eligible if salary > 50,000
    """
    return employee["salary"] > 50000

eligible_employees = list(filter(is_salary_eligible, employees))

print("Eligible Employees:")
for emp in eligible_employees:
    print(f"Name: {emp['name']}, Salary: {emp['salary']}")
