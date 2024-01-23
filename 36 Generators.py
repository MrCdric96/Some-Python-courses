# Generators in Python
def new(dict):
    for x,y in dict.items():
        yield x,y


a = {1:"Hi", 2:"Welcome"}
b = new(a)
print(next(b))
print(next(b))


def my_func(i):
    while i <= 3:
        yield i 
        i += 1


j = my_func(2)
print(next(j))
print(next(j))



def ex():
    n = 3
    yield n
    n = n * n
    yield n 

v = ex()
print(next(v))
print(next(v))