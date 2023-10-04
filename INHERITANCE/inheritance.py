# 1. SINGLE INHERITANCE

class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")


class Programmer(Employee):
    language = "python"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programmer")   # this gets the precedence


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)


# 2.MULTIPLE INHERITANCE

class Employee:
    company = "Visa"
    ecode = 120


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level += 1


class Programmer(Employee, Freelancer):
    name = "Nikhs"


p = Programmer()
p.upgradeLevel()
# visa will be printed because in class Programmer, Employee is written first
print(p.company)
print(p.level)


# 3.MULTILEVEL INHERITANCE
class Employee:
    country = 'India'

    def takeBreath(self):
        print("I am breathing")


class Programmer(Employee):
    company = "Facebook"

    def getSalary(self):
        print(f"Salary for employee:{self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am breathing, breathing!")


class Tester(Programmer):
    company = "Microsoft"

    def getSalary(self):
        print("Salary")


e = Employee()
p = Programmer()
t = Tester()

print(p.country)
p.salary = 100
p.takeBreath()
p.getSalary()
print(t.country)
t.takeBreath()
