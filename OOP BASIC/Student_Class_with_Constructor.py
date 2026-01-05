class student:

    company_name="MICROSOFT"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(f"name={self.name} \nroll no.={self.roll} \ncompany name={student.company_name}")

s1=student("satyam anmol",1)
s1.display()
        