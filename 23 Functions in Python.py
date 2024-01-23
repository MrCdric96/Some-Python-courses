def func1(name):
    return f"Hello {name}"


def func2(name):
    return f"{name}, how are you doing ?"


def func3(func4):
    return func4("Dear Learner")


print(func3(func1))
print(func3(func2))

# Multiple functions inside function

def func():
    print("Firts function")
    def inside_func1():
        print("First child function")
    def inside_func2():
        print("Second child function")

    inside_func2()
    inside_func1()

func()

# One more example

def my_function(n):
    def my_under_func1():
        return "Edureka"
    def my_under_funct2():
        return "Python"
    if n == 1:
        return my_under_func1
    else:
        return my_under_funct2
    
a = my_function(1)
b = my_function(2)

print(a())
print(b())

