def test():
    print('Hello world')


test()  # Hello world


# parameterized function
def abc(a):
    print(a + 10)


abc(10)  # 20


# optional parameters or default parameter
def getCountryName(name="USA"):
    print(name)


getCountryName()  # USA
getCountryName("UK")  # UK
getCountryName(100)  # 100


# pass a list of a function
def getNames(list):
    for x in list:
        print(x)


names = ['Java', 'Python', 'Javascript', 'C#']
getNames(names)


# Java
# Python
# Javascript
# C#


# function with return
def sum(a, b):
    return a + b


c = sum(10, 20)
print(c)


#
def getCapitalName(countryName):
    if countryName == "US":
        return "D.C"
    elif countryName == 'French':
        return "Paris"


print(getCapitalName("US"))


# Recursion in Python --- a function call itself
# WAP tp get the factorial of a given number:
# fact(4) = 4 * 3 * 2 * 1

def fact(num):
    if num > 1:
        num = num * fact(num - 1)
    return num


print(fact(10))  # 3628800


#
def login(username, password):
    print("login with %s and %s  " % (username, password))


login("Enver", "test@121212") # login with Enver and test@121212  
