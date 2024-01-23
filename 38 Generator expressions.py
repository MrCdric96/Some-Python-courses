f = range(6)
print("List comprehension",end=":")
q = [x + 2 for x in f]
print(q)

print("Generator expression",end=":")
r = (x + 2 for x in f)
print(r)

for x in r:
    print(x)


print("Generator expression", end=":")
r = (x + 2 for x in f)
print(r)
print(min(r))