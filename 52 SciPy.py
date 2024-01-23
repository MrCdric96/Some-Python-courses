"""What is SciPy ?
- SciPy is a Python library used to solve scientific and mathematical problems
- Built on Numpy
- Allows manipulations and visualizing

Numpy vs SciPy

- Numpy and SciPy used for mathematical and numerical analysis
- Numpy contains array data and basic operations
- SciPy consists of all the numerical code
- SciPy contains fully-featured versions of mathematical and scientific functions 
"""
#from scipy import cluster

#print(help(cluster))
#print(help())

# Special functions : Exponential functions and trigonometric functions 
from scipy import special
# Exponential functions
a = special.exp10(2)
print(a)

b = special.exp2(3)
print(b)

# Trigonometric functions

c = special.sindg(90)
print(c)

d = special.cosdg(90)
print(d)

# Integration fuctions : General Integration and Double integration 
"""Integration deals with adding slices to determine the whole.
Integration can be used to find displacement, area, etc.
General integration : the quad function caculates the integral of a function which has one variable.
Double Integration : the dblquad function calculates double integral of a function which has two variables. 
"""
from scipy import integrate

#print(help(integrate))
#print(help(integrate.quad))

#i= scipy.integrate.quad(lambda x:special.exp10(x), 0,1)
#print(i)

e = lambda x, y: x*y**2
f = lambda x: 1
g = lambda x: -1

print(integrate.dblquad(e, 0, 2, f, g))

# Fourier Transformations
"""Fourier transformation is a method that deals with expressing a function as a sum of periodic 
components and recovering the signal from those componets
"""
from scipy.fftpack import fft, ifft
import numpy as np 

x = np.array([1, 2, 3, 4])
#y = fft(x)
y = ifft(x)
print(y)

# Linear Algebra
"""SciPy is built on ATLAS LAPACK and BLAS libraries and is extramely fast in solving problems related to linear algebra.
Iverse of a matrix : inverse of a matrix B such that AB =| where | is the identity matrix consisting of ones down the main diagonal denoted as B = A¯¹
"""
from scipy import linalg
l = np.array([[1, 2], [3, 4]])
r = linalg.inv(l)
print(r)








