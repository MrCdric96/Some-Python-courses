# Accessing keys and values in a dict : Not compatible with Python 2
y = {"pork":25.3, "beef":33.8, "chicken":22.7}
print(y.keys())
print(y.values())
print(y.items())     # Key-value pairs

#check membership in y_keys  (only looks keys, not values)
print("beef" in y)

# check membership in y_values
print("calms" in y.values())
