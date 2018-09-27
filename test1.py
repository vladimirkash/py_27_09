# py_27_09
myList = list(str(input()))
length = len(myList)
a = ''
b = ''
counter = 1
x = ''
for p in myList:
    b = p
    if a != b:
        if a != '':
            print(a, counter)
            a = b
            counter = 1
        else:
            a = b
    else:
        counter = counter + 1
print(a, counter)
