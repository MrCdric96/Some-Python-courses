def pattern(n):
    k = 2 * n - 2
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x = x + 1
        for j in range(0, k):
            print(end=" ")
        k = n - 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")
    k = n - 2
    x = 65
    for i in range(n, -1, -1):
        ch = chr(x)
        x = x + 1
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print("\r")

pattern(10)