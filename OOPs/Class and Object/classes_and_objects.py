# Python is Object Oriented Programming
# Almost everything in python is an Object with it's properties and methods
# Objects are real world Entities
# Class are group of these Entities
# A class is like a bluprint or template for ctrating objects

class Employee:
    department = "IT"                                                    # variable

    def putdata(self):                                                   # Method 1
        self.id = int(input("Enter Employee id : "))
        self.name = input("Enter Employee Name : ")
        self.salary = float(input("Enter Employee Salary : "))

    def display(self):                                                   # Method 2
        print("Employee id: ", self.id)
        print("Employee name: ", self.name)
        print("Employee salary: ", self.salary)

# Objects
a = Employee()
print(a.department)
a.putdata()
a.display()
