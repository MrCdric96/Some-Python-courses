# Wile loop
import random

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0

while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulations, You made it!")
    
# For loop

fruits = ["Mango", "Grapes", "Apple"]
for fruit in fruits:
    print("Current fruit:&&", fruit)

num = int(input("Number: "))
factorial = 1

if num < 0:
    print("Must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)