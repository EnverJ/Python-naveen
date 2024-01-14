count = 0
while count < 10:
    # print("Hello world")
    print(count)
    count = count + 1

print("-------------")

# while else

number = 0
while number < 3:
    print("Hello Python")
    number = number + 1
else:
    print("Bye Python")

print("----------for loop--------")
# for loop;
name = ['Java', 'Python', 'dot net', 'C#']
for i in name:
    print(i)

# str
str = 'I love Python'
for i in str:
    print(i)

# list
list = ['Enver', 'Automation', 'Lab']
for index in range(len(list)):
    print(list[index])
# Enver
# Automation
# Lab

# for loop with else
CountryList = ['USA', 'AUS', 'UK', 'CAN']
for index in range(len(CountryList)):
    print(CountryList[index])
else:
    print("Country list is over")

cityList = ["Denver", "LA", "NY", "SF"]
for index in range(3):
    print(cityList[index])
else:
    print("City is over")

print("-----nested for loop-------")
# nested for loop
for i in range(1, 5):
    for j in range(i):
        print(i, end='')
    print()
# 1
# 22
# 333
# 4444
