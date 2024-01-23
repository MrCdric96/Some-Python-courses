# Lambda arguments : expression
x = lambda a: a * 2
print(x(3))

# Lambda within user-defined functions

def A(x):
    return(lambda y: x + y)

t = A(4)
print(t(8))

# Using lambda function within : filter(), map() and reduce()

# filter() : is used to filter the given iterables(lists, sets, etc) with the help of another function passed as an argment to test all the elements to be true or false
filter_list = [1, 2, 3, 4, 5, 6]
my_new_filter_list = list(filter(lambda a: (a/3==2), filter_list))
print(my_new_filter_list)

# map() : Applies a given function to all the iterables and returns a new list
map_list = [1, 2, 3, 4, 5, 6]
p = list(map(lambda a: (a/3!=2), map_list))
print(p)

# reduce() : applies some other function to a list of elements that are passed as a parameter to it and finally returns a single value
from functools import reduce
r = reduce(lambda a,b: a + b, [23, 56, 43, 98, 1])
print(r)

