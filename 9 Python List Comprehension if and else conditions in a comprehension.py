# if-else in a comprehension : must come before iteration
nums = [5, 3, 10, 18, 6, 7]
new_list = [x if x%2==0 else 10*x for x in nums]
print("new_list : " + str(new_list))