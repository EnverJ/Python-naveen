# no need to declare any type of variables
a = 123
print(a)

a = a + 0.1
print(a)

a = "test"
print(a)

x = 50
y = x
print(x)
print(y)
print(id(x))  # 4324152360
print(id(y))  # 4324152360

# A-Z a-z 0-9
min_bal = 100
print(min_bal)
number_of_month = 12  # _ is recommended
numberOfMonth = 12
print(number_of_month, numberOfMonth)

miles = 100.0
name = "Tom"
print(miles, name)

# Multiple assignment
a = b = c = 1
print(a, b, c)  # 1 1 1
a, b, c = 3, 4, "Sky"
print(a, b, c)  # 3 4 Sky

# Concatenations
s1 = "Hello world"
print(s1)  # Hello world
print(s1[0])  # H
print(s1[2:6])  # llo
print(s1[2:])  # llo world
print(s1 * 2)  # Hello worldHello world
print(s1 + " " + "Python")  # Hello world Python
