# Delete an item from a list
import random 

letters = [x for x in "ABCDEF"]
random.shuffle(letters)
letrs = [a for a in letters if a != "C"]
print(letters, letrs)
