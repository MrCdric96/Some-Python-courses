# Reduce function
from functools import reduce

def a(x, y):
    return x + y

s = reduce(a, [1,3,4,5,6,7,7,8,8])
print(s)

l = reduce(lambda q,p: q*p, [1,2,3,4,5,6,7,7])
print(l)