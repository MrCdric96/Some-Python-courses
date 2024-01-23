from math import sqrt

n = int(input("Maximal Number: "))
for a in range(1, n + 1):
    for b in range(a, n):
        c_quare = a ** 2 + b ** 2
        c = int(sqrt(c_quare))
        if ((c_quare - c ** 2) == 0):
            print(a, b, c)