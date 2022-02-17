class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class Student(Person):
    def __init__(self, name, age, section):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Section: ", self.section)


P = Person("Ralph", 12)
P.display()
print("------------------")
S = Student("Joan", 13, "Section A")
S.displayStudent()
