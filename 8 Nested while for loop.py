travelling = input("Yes or No: ")

while travelling == "Yes":
    num = int(input("number of people travelling: "))

    for num in range(1, num + 1):
        name = input("Enter name: ")
        age = input("Enter age: ")
        sex = input("Enter sex: ")

        print(name)
        print(age)
        print(sex)

    travelling = input("Oups! forgot someone.")

