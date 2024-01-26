# Iterating a dict : note, items are in random order
y = {"pork":22.3, "beef":333.8, "chicken":22.7}

for key in y:
    print(key, y[key])

for k, v in y.items():
    print(k, v)
