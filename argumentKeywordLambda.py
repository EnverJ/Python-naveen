def login(username, password):
    print(username, password)


# key and value pair
login("Enver", "12313fsfs")
login(username="Enver", password="12313fsfs")


# * argument
def getMarks(*arg):
    for x in arg:
        print(x)


getMarks(10, 20, 20, 30, 90)  # 10, 20, 20, 30, 90
getMarks('A', 'B', 'C')  # A B C


# Keyword args:
# **arg
def getStudentMarks(**args):
    for key, value in args.items():
        print("%s==%s" % (key, value))


getStudentMarks(enver=100, tom=70, peter=20)
# enver==100
# tom==70
# peter==20
getStudentMarks(key="apple", sellerName="John")

# key==apple
# sellerName==John

# lambda functions: Anonymous function:
# a fun without any name
cube = lambda x: x * x * x
print(cube(4))  # 64

total = lambda marks: marks + 30
print(total(100)) # 130
