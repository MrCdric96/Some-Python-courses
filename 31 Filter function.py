# Filter 
def new1(i):
    if i >= 3:
        return i 
    
j = filter(new1,(1,2,3,4,5,6,7))
print(j)
print(tuple(j))

z = filter(lambda x: (x >= 3),(1,2,3,4,5,6,7))
print(list(z))