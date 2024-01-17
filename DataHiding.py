class Employee:
    # define a hidden member of employee class
    __salary = 100


e1 = Employee()
# print(e1.__salary)  # 'Employee' object has no attribute '__salary'.  this is not hte wright way to accessing hiding values


# access private hidden variable by using tricky syntax:
print(e1._Employee__salary)  # 100



