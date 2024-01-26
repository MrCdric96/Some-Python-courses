# Nested loop iteration for 2D list : b is the subsets, x is the values
a = [[1, 2], [3, 4]]
new_list = [x for b in a for x in b]
print(new_list)