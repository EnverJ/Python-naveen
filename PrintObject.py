# string representation of class object
class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "a:%s b:%s" % (self.x, self.y)

    def __str__(self):
        return "value of a is %s and b is %s" % (self.x, self.y)


# Test Code
t = Test(10, 20)  # this will call __str__ method
print(t)  # value of a is 10 and b is 20

