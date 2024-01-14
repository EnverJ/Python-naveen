name = 'Alexander'
for i in name:
    print(i)
    if i == "x":
        break
name = 'Alexander'
for i in name:
    print(i)
    if i == "x":
        continue

str = ['pyhon', 'java', 'C#', 'JavaScript']
for l in range(len(str)):
    print(str[l])
    if str[l] == 'java':
        print('I found java')
        break

lang = ["Uyghur", "English", "French", "Spanish"]
flag = False
for index in range(len(lang)):
    print(lang[index])
    if lang[index] == "English":
        print("English s most popular language in the world")
        flag = True
        break
if flag:
    print("I want to learn English")
