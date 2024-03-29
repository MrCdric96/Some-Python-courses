import functools

def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, *kwargs)
        return wrapper.instance 
    wrapper.instance = None
    return wrapper 

@singleton
class one:
    pass

first = one()
second = one()

print(first is second)