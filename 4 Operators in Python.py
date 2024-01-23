print("Arithmetic operators")
x = 20
y = 10

print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print( x // y)
print(x % y)

print("assignment operator")

a = 5
a += 5
print(a)
a **= 5
print(a)

print("comparison operators")

val = 10
num1 = 20
compare1 = val == num1
compare2 = val < num1
compare3 = val > num1
print(compare1)
print(compare2)
print(compare3)

print("condition statement")

if val == num1:
    print("equal")
elif val > num1:
    print("greater")
else:
    print("smaller")

print("logical operators")

z =  10
an = z > 10 and x < 5
az = z > 10 or x < 5
print(an)
print(az)

nt = not(z > 10 and x < 5) 
print(nt)

print("identity operators")

list1 = [10, 20, 30]
list2 = [10, 20, 30]

l = list1
print(l is list1)
print(list1 is list2)
print(list1 is not list2)

print("membership operator")

print(l in list1)
print(list1 in list2)
print(10 in list1)
print(list1 == list2)

print("bitwise operators")

print(10 & 12) # bitwise AND
print(10 | 12) # bitwise OR
print(10 >> 2) # Left Shift
print(10 << 2) # Right Shift

