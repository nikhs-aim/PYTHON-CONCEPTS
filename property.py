class Employee:
    company = "Bharath Gas"
    salary = 200
    salaryBonus = 400

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus


e = Employee()
print(e.totalSalary)
