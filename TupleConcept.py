# Tuple : is a collection of elements of any python data type
# Tuple vs list
# 1. syntax: you have to store the values in a tuple wit (), but in list: []
# 2. Tuple is immutable (value cannot be changed) but List is mutable

marks = (100, 90, 20, 45)
employeeData = ("Tom", 34, 'm', 23.2, True)
print(employeeData)  # ('Tom', 34, 'm', 23.2, True)
print(employeeData[0])  # Tom
# print(employeeData[5])  # tuple index out of range
print(employeeData[-1])  # True

# list is mutable
list = [10, 20, 30, 40]
list[1] = 100
print(list)  # [10, 100, 30, 40]

# tuple immutable
# names2 = ("Ruby", " Python", "Java", "C#")
# names2[2] = "English"
# print(names2)   #  'tuple' object does not support item assignment

names = ("Ruby", " Python", "Java", "C#")
# del names
# print(names)  #  name 'names' is not defined

# concatenations
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
print(t1 + t2)  # (1, 2, 3, 4, 5, 6, 7, 8)

t3 = (1, 2, 3)
print(t3 * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# range slicing
t4 = (1, 2, 3, 4, 5, 6, 7)
print(t3[1:3])  # (2, 3)

# in:
employeeData1 = ("Tom", 34, 'm', 23.2, True)
print(34 in employeeData1)  # True
print(33 in employeeData1)  # False
# not in
print(33 not in employeeData1)  # True
# len
length = len(employeeData1)
print(length)  # 5
# max
number = (1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 10)
print(max(number))  # 10

#
names1 = ("abc", " efg", "hij")
print(max(names1))  # hij

# min
print(min(number))  # 1
