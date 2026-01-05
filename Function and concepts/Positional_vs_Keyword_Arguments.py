def employee_details(emp_id, name, role):
    print("Employee ID:", emp_id)
    print("Name:", name)
    print("Role:", role)

employee_details(101, "Satyam", "Python Developer")#calling with positional arguments
employee_details(name="Satyam", role="Python Developer", emp_id=101) # calling with keywors argyuments


