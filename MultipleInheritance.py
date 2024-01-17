# Multiple inheritance is not allowed in java. but it is allowed in Python
class Base1(object):
    def __init__(self):
        self.str1 = "Enver"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Ron"
        print("Base2")


class Child(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Child")

    def printString(self):
        print(self.str1, self.str2)


ob = Child()
ob.printString()

# Base1
# Base2
# Child
# Enver Ron
