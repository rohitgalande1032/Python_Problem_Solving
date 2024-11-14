# When you run the above code first of all it will create the Empty Object in memory named by first_student
# After it call the __init__ or dunder
# Initialize all the values/data provided by object will store in attributes and perform some actions like average()

class Student:
    def __init__(self, my_role, my_name, my_marks):   # Constructor
        self.rollno = my_role
        self.name = my_name
        self.marks = my_marks

    def average(self):  #Method
        print(sum(self.marks) // len(self.marks))

first_student = Student(1, "Ronit", [88, 90, 89, 98, 99])  #Object
print(f"Average marks of {first_student.name} : ")
first_student.average()