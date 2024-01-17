# set is not order based
# it stores different type of data
# it performs different mathematical operations
# it is not store duplicate elements
# define a set: use {}
# it does not start any duplicate values
s1 = {100, "Tom", True, 12.33}
s2 = {100, 200, 100, 200, 300}
print(s2)  # {200, 100, 300}
print(s1)  # {True, 100, 12.33, 'Tom'}

# set() Function. set is not ordered based
s3 = set("Python")
print(s3)  # {'y', 'h', 'o', 'n', 'P', 't'}

s4 = set([30, 40, 20, 20, 34])
print(s4)  # {40, 34, 20, 30} 3 duplicated value will be removed.

# tuple
s5 = set((10, 20, 30, 40))
print(s5)  # {40, 10, 20, 30}

# while creating a set object, you can store only numbers, String, tuple
# List and dictionary are not allowed.

set1 = {(10, 20), 30, 40}
print(set1)  # {40, 30, (10, 20)}
# list won't work
# set2 = {[10, 20], 30, 40}
# print(set2)  # TypeError: unhashable type: 'list'

# Set operations;
# union: |
p1 = {1, 2, 3, 4}
p2 = {5, 6, 7, 8}
print(p1 | p2)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(p1.union(p2))  # {1, 2, 3, 4, 5, 6, 7, 8}

# intersections: & --> common properties
p3 = {1, 2, 3, 4, 5, 6}
p4 = {5, 6, 7, 8}
print(p3 & p4)  # {5, 6}
print(p3.intersection(p4))  # {5, 6}

# difference of sets:
p5 = {1, 2, 3, 4, 5, 6}
p6 = {5, 6, 7, 8, 9, 10}
print(p5 - p6)  # {1, 2, 3, 4}
print(p6 - p5)  # {8, 9, 10, 7}
print(p5.difference(p6))  # {1, 2, 3, 4}
print(p6.difference(p5))  # {8, 9, 10, 7}

# systematic difference: ^
# exclude the common elements
p7 = {1, 2, 3, 4, 5, 6}
p8 = {5, 6, 7, 8, 9, 10}
print(p7 ^ p8)  # {1, 2, 3, 4, 7, 8, 9, 10}
print(p7.symmetric_difference_update(p8))  # None

# Set - In Build methods:
# 1. add():
s1 = {"Java", " Python", "C++"}
s1.add("Perl")
print(s1)  # {'Perl', 'Java', 'C++', ' Python'}

# 2. update
s2 = {"Java", " Python", "C++"}
s2.update(["C", "GO"])
print(s2)  # {' Python', 'C++', 'Java', 'GO', 'C'}
s2.update(("Ruby", "JavaScript"))
print(s2)  # {'JavaScript', 'Java', ' Python', 'GO', 'C', 'Ruby', 'C++'}

# 3. clear
print(s2.clear())  # None

# 4. Copy
lang = {"Java", "GO", "Perl"}
lang1 = lang.copy()
print(lang1)  # {'Java', 'GO', 'Perl'}

# 5. Discard:
lang = {"Java", "GO", "Perl"}
lang.discard("GO")
print(lang)  # {'Java', 'Perl'}

# 6. Remove:
student = {"Naveen", "Tom", "Enver", "Peter"}
student.remove("Tom")
print(student)  # {'Enver', 'Naveen', 'Peter'}
# student.remove("John")
# sprint(student)  # KeyError: 'John'
