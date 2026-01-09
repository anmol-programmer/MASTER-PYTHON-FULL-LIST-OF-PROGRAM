class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = None

    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print("Marks stored successfully")
        else:
            print("Invalid marks Enter value between 0 and 100")

    def get_marks(self):
        if self.__marks is None:
            print("Marks not set yet")
        else:
            print("Student marks are", self.__marks)
name = input("Enter student name: ")
student = Student(name)

while True:
    print("\nStudent Menu")
    print("1 Enter marks")
    print("2 View marks")
    print("3 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        marks = int(input("Enter marks: "))
        student.set_marks(marks)

    elif choice == "2":
        student.get_marks()

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice")
