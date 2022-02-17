"""
How to use __init___ method to assign
values to data attributes.

Delete version
"""


class Employee:
    def __init__(self, salary, name):
        self.salary = salary
        self.name = name


emp1 = Employee(10000, "ralph")
print(emp1.salary)
print(emp1.name)

del emp1.salary  # deletes the object property
del emp1  # del the object

print(emp1.salary)
print(emp1.name)
