def ex():
    n = 3
    yield n
    n = n * n 
    yield n


v = ex()
for x in v:
    print(x)