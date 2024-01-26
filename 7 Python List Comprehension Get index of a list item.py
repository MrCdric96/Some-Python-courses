# Get index of a list item 
names = ["Cosmo", "Pedro", "Anu", "Ray"]
idx  = [k for k, v in enumerate(names) if v == "Ray"]
print("index = " + str(idx[0]))