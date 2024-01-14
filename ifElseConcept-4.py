x = int(input("please enter a value of x"))

if x < 0:
    print(" x is negative number")
elif x == 0:
    print("x is 0")
elif x > 0:
    print("x is greater than 0")
else:
    print("x is not defined")

# dead code
if True:
    print("PASS")

# else:  # dead code . unreachable code
#    print("Fail")

#
if 10 > 5:
    print("Hi")

# write a program to find out the highest number
a = 100
b = 4200
c = 300
d = 10000
if a > b and a > c and a > d:
    print("a is highest number")
elif b > c and b > d:
    print("b is the highest number")
elif c > d:
    print("c is the highest number")
else:
    print("d is the highest number")

#
total = int(input("enter the total value"))
if total < 100:
    total = total + 20
elif 100 <= total <= 500:
    total = total + 50
else:
    total = total + 100
print(total)
# print("total" + total)  # TypeError: can only concatenate str (not "int") to str

# str method
print("total is " + str(total))
# f'{}{}'  f string
print(f'{"total value is "}{total}')
