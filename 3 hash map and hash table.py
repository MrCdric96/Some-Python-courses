my_dict = {"Dave" : "001", "Ava" : "002", "Joe" : "003"}
print(my_dict)
print(type(my_dict))

new_dict = dict()
print(new_dict)
print(type(new_dict))

new_dict = dict(Dave="001", Ava="002", Joe="003")
print(new_dict)

# Nested dictionnaries
emp_details = {"Employee":{"Dave":{"ID":"001", "Salary":"2000", "Designation":"Team Lead"},
                           "Ava":{"ID":"002", "Salary":"1000", "Designation":"Associate"},
                           "Joe":{"ID":"003", "Salary":"1000", "Designation":"Associate"}}}

print(emp_details)

# Accessing items
print(my_dict["Dave"])
print(my_dict.keys())
print(my_dict.values())

print(my_dict.get("Dave"))
print(my_dict.get("Ava"))
print(my_dict.get("Joe"))

for x in my_dict:
    print(x)

for y in my_dict.values():
    print(y)

for a, b in my_dict.items():
    print(a, b)

# Updating
my_dict["Dave"] = "004"
my_dict["Chris"] = "005"
print(my_dict)

# Deleting
my_dict.pop("Ava")
print(my_dict)

my_dict.popitem()
print(my_dict)

del my_dict["Dave"]
print(my_dict)

# Coverting a dictionnary to a data frame

import pandas as pd
df = pd.DataFrame(emp_details["Employee"])
print(df)
