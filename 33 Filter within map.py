# filter within map
c = map(lambda x: x+x, filter(lambda x:(x>=4), [2,3,4,5]))
print(tuple(c))