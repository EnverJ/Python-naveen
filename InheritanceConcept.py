# object is a super class
class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


# Employee class inherited from Person
class Employee(Person):
    def isEmployee(self):
        return True


# Test Person
emp = Person("Enver")
print(emp.name)  # Enver
print(emp.getName(), emp.isEmployee())  # Enver False

emp1 = Employee("Todd")
print(emp1.name)  # Todd
print(emp1.getName(), emp1.isEmployee())  # Todd True
