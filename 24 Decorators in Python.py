# Basic example
def function1(function):
    def wrapper():
        print("Hello!")
        function()
        print("Welcome to Python Edureka tutorial !")
    return wrapper


@function1
def function2():
    print("Pythonista")


function2()

# Python decorator with arguments
def my_dec_func(func):
    def my_wrapper(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Welome to turing developers")
    return my_wrapper


@my_dec_func
def my_dec_func2(name):
    print(f"Cogratulations {name}, you have succeded to the Python coding challenge!")


my_dec_func2("Cédric")

# Returning values from a decoratored function
def my_returning_val(funct):
    def my_wrapper_val(*args, **kwargs):
        print("It worked!")
    return my_wrapper_val


@my_returning_val
def my_returning_val2(name2):
    print(f"You are hired {name2} !")


my_returning_val2("Cédric")


