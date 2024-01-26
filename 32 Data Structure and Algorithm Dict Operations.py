# Dict operations 
x = {"pork":25.3, "beef":33.8, "chicken":22.7}
x["shrimp"] = 38.2   # add or updat
print(x)

# delete an item
del (x["shrimp"])
print(x)

# get lenght of dict x
print(len(x))

# delete all items from dict x
x.clear()
print(x)

# delete dict x
del x
