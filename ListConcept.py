# concept 3
score = [10, 23, 13, 25, 49]
print(score)  # [10, 23, 13, 25, 49]

#
print(score[0])  # 10
# print(score[5])  # list index out of range
print(score[-1])  # 49
print(score[-5])  # 10

# 0 - 4, slicing
# -1, -2 -3 -4
print(score[:])  # [10, 23, 13, 25, 49]  # new / shallow copy of list

# concatenation
print(score + [1, 2, 3])  # [10, 23, 13, 25, 49, 1, 2, 3]
print(score + ['a', 'v', 'c'])  # [10, 23, 13, 25, 49, 'a', 'v', 'c']

# list is mutable
number = [1, 2, 3, 4, 5, 6]
number[2] = 90
print(number)  # [1, 2, 90, 4, 5, 6]

# append()
number.append(100)  # 100 will be appended to the end
print(number)  # [1, 2, 90, 4, 5, 6, 100]

number.append(7 ** 3)
print(number)  # [1, 2, 90, 4, 5, 6, 100, 343]

name = ['a', 'b', 'c', 'd', 'f']
print(name)  # ['a', 'b', 'c', 'd', 'f']

name[2:5] = ['C', 'D', 'F']
print(name)  # ['a', 'b', 'C', 'D', 'F']

# remove
name[2:5] = []
print(name)  # ['a', 'b']
# make it empty
name[:] = []
print(name)  # []

name.append([1, 2, 3])
print(name)  # [[1, 2, 3]]

test = [2, 3, 4, 5, 6]
print(len(test))  # 5

# nested lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  # ['a', 'b', 'c']
print(x[1])  # [1, 2, 3]
print(x[0][1])  # b
print(x[1][2])  # 3
