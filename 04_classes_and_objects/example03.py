# Create and call method of a class
class Employee:
    name = "ralph"
    salary = 1000

    def tax(self):
        print(self.salary * 0.10)


emp1 = Employee()
print(emp1.salary)
print(emp1.name)
emp1.tax()
