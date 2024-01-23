"""What is Numpy ? 
Numpy is the core library for scientific computing in Python.
It provides a high-performance multidimensional array object, and tools for working with these arrays.
"""
import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)

"""Numpy vs List
Advantages of Numpy over List : Less memory, Fast, Convenient
"""
import time 
import sys

s = range(1000)
print(sys.getsizeof(5) * len(s))

d = np.arange(1000)

print(d.size * d.itemsize)

size = 1000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()

result = [(x,y) for x, y in zip(l1, l2)]
print((time.time() - start) * 1000)


start = time.time()

result = a1 + a2

print((time.time() - start) * 1000)


"""Numpy Operations"""

x = np.array([(1, 2, 3), (2, 3, 4)])
print(x.ndim)
print(x.itemsize)
print(x.dtype)

y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(y.size)
print(y.shape)

z = np.array([(1, 2, 3, 4), (3, 4, 5, 6), (7, 8, 9, 10)])
#z = z.reshape(4, 2)
#print(z)

"""Slicing"""

print(z[0,2])
print(z[0:2,3])

xy = np.linspace(1, 3, 10)
print(xy)

"""Others operations with numpy"""

xz = np.array([1, 2, 3])
print(xz.max())
print(xz.min())
print(xz.sum())

yz = np.array([(1, 2, 3), (3, 4, 5)])

print(yz.sum(axis=0))
print(yz.sum(axis=1))

print(np.sqrt(yz))
print(np.std(yz))

az = np.array([(1, 2, 3), (3, 4, 5)])

print(yz + az)
print(yz - az)
print(yz * az)
print(yz / az)

print(np.vstack((yz, az)))
print(np.hstack((yz, az)))

print(az.ravel())





