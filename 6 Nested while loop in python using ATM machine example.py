# Nested loop : Python allows use of loop inside another loop. This is called Nested Loop 
print("Welcome to Kivucian Bank ATM")
restart = ("Y")
chances = 3
balance = 500000
while chances >= 0:
    pin = int(input("Enter your 4 digit pin: "))
    if pin == (1234):
        print("You entered your pin correctly\n")
        while restart not in ("n", "NO", "no", "N"):
            print("Press 1 for your balance\n")
            print("Press 2 to make a withdraw\n")
            print("Press 3 to pay in\n")
            print("Press 4 to return card\n")
            option = int(input("What would you like to choose? "))
            if option == 1:
                print("Your balance is $", balance, "\n")
                restart = input("Would you like to go back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank you!")
                    break
            elif option == 2:
                option2 = ("y")
                withdrawl = float(input("How much would you like to withdrwal ? \n$100/$200/$300/$400/$500/$600/$700/$800/$900/$1000: "))
                if withdrawl in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
                    balance = balance - withdrawl
                    print("\nYour balance is now $", balance)
                    restart = input("Would you like to go back? ")
                    if restart in ("n", "NO", "no", "N"):
                        print("Thank you!")
                        break
                elif withdrawl != [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
                    print("Invalid amount, Please re-try\n")
                    restart = ("y")
                elif withdrawl == 1:
                    withdrawl = float(input("Enter desired amount: "))
            
            elif option == 3:
                Pay_in = float(input("How much would you like to Pay-in? "))
                balance = balance + Pay_in
                print("\nYour balance is $", balance)
                restart = input("Would you like to go back? ")
                if restart in ("n", "NO", "no", "N"):
                    print("Thank you!")
                    break
            elif option == 4:
                print("Please wait while your card is returned...\n")
                print("Thank ypu for your service!")
                break
            else:
                print("Please enter a correct number.\n")
                restart = ("y")
    elif pin != ("1234"):
        print("Incorrect password")
        chances = chances - 1
        if chances == 0:
            print("\nNo more tries")
            break




