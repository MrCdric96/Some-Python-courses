# Number pattern
def pattern(n):
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")

pattern(7)

# Pascal's triangle

def pascal_triangle(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i,j), " ", end="")
        print()

def function(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res 

pascal_triangle(7)

def pattern1(n):
    x = 0
    for i in range(0, n):
        x = x + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")

pattern1(10)

def descending_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("\r")

descending_pattern(10)

def pyramiid_pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("10", end="")
        print("\r")

pyramiid_pattern(5)  

def diamond_pattern(n):
    k = 2 * n - 2
    x = 0
    for i in range(0, n):
        x = x + 1
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")

    k = n - 2
    x = 0
    for i in range(n, -1, -1):
        x = x + 1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(x, end=" ")
        print("\r")

diamond_pattern(7)

def pattern2(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("\r")

pattern2(5)

def binary_numbers(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("10", end="")
        print("\r")

binary_numbers(5)



        