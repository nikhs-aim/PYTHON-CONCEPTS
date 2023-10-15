# solving a problem by creating objects
# It implements DRY principle (Do not repeat yourself)
# Class - blueprint for creating objects
# Objects - instantiation of class
# Objects of a given class can invoke its method without revealing the implementation details to the user - abstraction and encapsulation
# Class attributes - attributes that belongs to a class rather than an object
# Instance attributes - attributes that belongs to an instance


# 1.RAILWAY EXAMPLE
class RailwayForm:
    formType = "Railway Form"

    def printDta(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


nikhsApplication = RailwayForm()
nikhsApplication.name = "nikhs"
nikhsApplication.train = "Shatabdhi express"
nikhsApplication.printDta()


# 2.EMPLOYEE EXAMPLE
class Employee:
    company = 'Google'
    salary = 100  # Instance attributes will be given importance, this is class attribute


harry = Employee()
nikhs = Employee()
harry.salary = 300  # Instance attribute
nikhs.salary = 400

print(harry.company)
print(nikhs.company)

Employee.company = 'Youtube'  # class attribute

print(harry.company)
print(nikhs.company)

print(harry.salary)
print(nikhs.salary)


# 3.SELF - If you want to represent an instance attribute or class attribute in a function.
# We can pass arguments along with self.
class Employee:
    company = "Google"

    def getSalary(self, sign):  # here self represents the object that you pass to the function, if you want to represent the attributes
        print(
            f"Salary for this employee in {self.company} is {self.salary},{sign}")


nikhs = Employee()
nikhs.salary = 100000
nikhs.getSalary("Thanks!")  # Employee.getSalary(nikhs)


# 4.static method
''' if we want to use self, then we have to pass the object when the function is called.
some times if we want to call a function without passing any objects, we should use @staticmethod'''


class Employee:
    @staticmethod
    def greet():
        print("Good morning")


Employee.greet()


# init method - this will run automatically, no need to call
# we can also give arguments
class Employee:
    def __init__(self, name, company):
        self.name = name  # set whatever we pass when called
        self.company = company
        print("Hello, how can I help you?")

    def getDetails(self):
        print(
            f"The name of the employee is {self.name} and belongs to {self.company}")


# objects can be instantiated like this using constructor
nikhs = Employee("nikhs", "Google")
nikhs.getDetails()
