"""Lets add title and labels to our graph"""
from matplotlib import pyplot as plt

x = [5, 8, 10]
y = [12, 16, 6]

plt.plot(x, y)

plt.title("info")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()