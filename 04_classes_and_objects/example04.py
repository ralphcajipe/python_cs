# How to use __init___ method to assign values to data attributes

class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name


emp1 = Employee(10000, "ralph")
print(emp1.salary)
print(emp1.name)

emp1.salary = 20000
print(emp1.salary)
