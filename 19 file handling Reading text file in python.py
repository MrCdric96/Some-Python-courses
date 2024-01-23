#Reading text file in python
import os

file = open("C:\\Users\\Sikabwe Cedric\\Desktop\\giraffe.txt", "r")
print(file.read())        #this will read all the file
#print(file.readline())    #this will only read the first line(sentence)
#print(file.readline(5))   #this will only read the 5 characters of the first line
#print(file.readlines())    #this will read all the file in one line
file.close()
#print(file.read(5)) #this will only read the 5 characters of the first line

#Looping over a file object