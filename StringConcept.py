# 2 ways to declare a string
s1 = "testing selenium"
s2 = 'Hello world'
print(s1, s2)  # testing selenium Hello world

print(s1[0])  # t
print(s1[12])  # n
# print(s1[100])  # string index out of range
print(s1 + " " + s2)  # testing selenium Hello worlds
# non-printable characters
print("hello\nworld")  # \n next line.
print('hello\tworld')  # hello	world
print("rest" * 5)  # restrestrestrestrest
print(s1[0:5])  # testi
print("test" in s1)  # True
print("Java" not in s1)  # True

# % formatting operators
print("my name is %s and my age is %d " % ("Tom", 23))  # my name is Tom and my age is 23

s3 = '''test java
test python
test selenium
this is my python selenium'''
print(s3)

# test java
# test python
# test selenium
# this is my python selenium

s4 = """hi this is my pyhon code 
and I am learning python 
and I am so happy"""
print(s4)
# hi this is my pyhon code
# and I am learning python
# and I am so happy

print('hi i\'m enver')  # hi i'm enver
print(
    "hi my gav programming langauge is \"ython\" and i am so happy")  # hi my gav programming langauge is "python" and i am so happy

# capitalize()
str = "this is my Python code"
print(str)  # this is my python code
print(str.capitalize())  # This is my python code
# count
print(str.count("Python"))  # 1
# find()
print(str.find("code"))  # 18
print(str.find("Code"))  # -1
# length()
print(len(str))  # 22
# lower(0
print(str.lower())  # this is my python code
# lstrip()
str1 = " hello "
print(str1.lstrip())  # hello
print(str1.rstrip())  # hello

# max() and min()
print(max(str1))  # o
print(min(str1))  # space

# replace()
str3 = "Hello Test Python"
print(str3.replace("Hello", "Bye"))  # Bye Test Python

# split()
str4 = "Java Hello Python Hello js"
str5 = str4.split("Hello")
print(str5)  # ['Java ', ' Python ', ' js']
print(str5[0])  # Java

# upperCase()
print(str4.upper())  # JAVA HELLO PYTHON HELLO JS

#
st = "Hello"
print(st[0])  # H
print(st[-5])  # H
print(st[-1])  # o

# string comparison
a = "test"
b = "test"
print(a is b)  # True
print(a == b)  # True

p = "test!"
q = "test!"
print(p is q)
print(p is not q)  # True
print(p == q)  # True

h = "US !"
g = "US !"
print(h == g)  # True
