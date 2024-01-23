# map(func, iterables)
def new(a):
    return a * a

x = map(new, [1,2,3,4])
print(list(x))


def new(a, b):
    return a * b

x = map(new,[1,2,3,4],[2,3,4,5])
print((x))
print((tuple)(x))

lst = [1,2,3,4,5]
y = list(map(lambda x: x + 3, lst))
print(y)

