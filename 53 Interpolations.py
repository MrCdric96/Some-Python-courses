# Interpolation functions
"""Interpolation functions refers to constructing new data points within 
a set of kwown data points. The scipy.interpolate consists of spline functions
and classes, one dimensional and multi-dimensional(univariate and multivariate) interpolation classes, etc.
"""
import matplotlib.pyplot as plt 
import numpy as np
from scipy import interpolate

x = np.arange(5, 20)
y = np.exp(x/3.0)
f = interpolate.interp1d(x, y)
x1 = np.arange(6, 12)
y1 = f(x1) # use interpolation function returned by interp1d
plt.plot(x, y, "o", x1, y1, "--")
plt.show()




