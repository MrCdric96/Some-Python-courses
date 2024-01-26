"""List :
General purpose
Most widely used data structure
Grow and shrink size as needed
Sequence type
Sorable
"""
# Constructors : creating a new list
x = list()
y = ["a", 25, "dog", 8.43]
tuple1 = (10, 20)
z = list(tuple1)

# List comprehension
a = [m for m in range(8)]
print(a)

b = [i**2 for i in range(10) if i>4]
print(b)

