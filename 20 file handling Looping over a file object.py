#Looping over a file object
import os 

file = open("C:\\Users\\Sikabwe Cedric\\Desktop\\giraffe.txt", "r")
for line in file:
    print(file.readlines())

file.close()
