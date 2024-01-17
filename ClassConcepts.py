class Car:
    # class variables
    wheels = 4

    # constructor
    #  overloading is not allowed. always consider the latest constructor
    def __init__(self):
        print("default constructor")

    def __init__(self, color):
        print("Car class constructor")
        self.color = color

    def test(self):
        print("test method")

    # any variable is decared inside the method or constructor: instance variable
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price


# how to create an Object of this class
# c1 = Car("Red")  # Car class constructor
# print(c1.wheels)  # 4
# print(Car.wheels)  # 4
# c1.test()  # test method
# c1.setPrice(1000)
# print(c1.getPrice())  # 1000

# c2 = Car(); # Car.__init__() missing 1 required positional argument: 'color'
c2 = Car("Black")  # Car class constructor


class Test:
    a = 10


# blank class
class Pop:
    pass


p1 = Pop()
