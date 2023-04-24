def decorator(func):
    def wrapper():
        print("Decoration starts")
        func()
        print("Decoration ends")
    return wrapper

@decorator
def func():
    print("I am the function gonna get decorated")

func ()