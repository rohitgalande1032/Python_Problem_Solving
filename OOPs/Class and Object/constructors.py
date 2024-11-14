# Constructors
# It is a special method within a class that gets automatically called when object is created
# It is used to initialize the attributes of the object
# It is written with __init__ . it also called as dunder


# Constructor function take data from user
class Faculty: 
    def __init__(self):
        self.id = int(input("Enter Faculty Id: "))
        self.name = input("Enter Faculty Name: ")
        self.salary = float(input("Enter Faculty Salary: "))

    def display(self):
        print("Faculty id: ", self.id)
        print("Faculty name: ", self.name)
        print("Faculty salary: ", self.salary)


# By Parameter passing to constructors
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee id: ", self.id)
        print("Employee name: ", self.name)
        print("Employee salary", self.salary)

# Faculty class
faculty1 = Faculty()
faculty1.display()

#Employee class
employee1 = Employee(1, "Ronit", 2000000)
employee1.display()