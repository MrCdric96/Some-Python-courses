# Fibonacci series
def fib():
    f, s=0, 1
    while True:
        yield f 
        f, s=s, f+s
for x in fib():
    if x > 50:
        break
    print(x, end=" ")
# Number Stream
a = range(2,100,2)
b = (x for x in a)
print(b)
for y in b:
    print(y)






