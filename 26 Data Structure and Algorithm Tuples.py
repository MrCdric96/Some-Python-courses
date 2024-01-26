"""Tuples:
Immutables(can't add/change)
Useful for fixed data
Faster than lists
Sequence type
"""
#Constructors : creating new tuples.

x = ()
x = (1, 2, 3)
x = 1, 2, 3 
x = 1, # The comma tells Python it's a tuple
print(x, type(x))

list1 = [2, 4, 6]
x = tuple(list1)
print(x, type(x))
