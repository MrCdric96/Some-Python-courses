# Sorting by the second letter : add a key parameter and lambda function to return the second character. (The word key here is defined parameter name, k is an arbitrary variable name)
z = ["Kevin", "Niklas", "Jenny", "Craig"]
print(sorted(z, key=lambda k:k[1]))