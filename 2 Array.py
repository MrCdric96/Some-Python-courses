import array

a = array.array("i", [1,2,3,4,5,6])
print(a)

# array as arr
import array as arr 
a = arr.array("i", [1,2,3,4,5,6])

# import all
from array import *

a = array("i", [12,3,4,5,6,5])
print(a)

# Accessing array elements
print(a[2])
print(a[-2])

# Finding lenght of an array
print(len(a))

# adding elements to an array : append(), extend(), insert()
a.append(8)
print(a)

a.extend([9,8,6,5,4])
print(a)

a.insert(2,6)
print(a)

# removing elements of an array : pop(), remove()

a.pop()
print(a)

a.pop(-2)
print(a)

a.pop(2)
print(a)

a.remove(8)
print(a)

# array concatenation 

b = arr.array("i", [1,2,3,4,5,6,7])
c = arr.array("i", [3,5,7,5,3,2,1])
d = arr.array("i")
d = b + c
print(d)

# slicing an array

print(d[0:5])
print(d[0:-2])
print(d[::-1])

# Looping : for and while
for x in d:
    print(x)

print("-----------------------------")

for x in d[0:-3]:
    print(x)

print("-----------------------------")

temp = 0
while temp < d[2]:
    print(d[temp])
    temp += 1

print("-----------------------------")

tem = 0
while tem < len(a):
    print(a[tem])
    tem += 1





