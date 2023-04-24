def decorator(func):
    def wrapper (wrapper_parameter):
        print("Function Begins")
        func(wrapper_parameter)
        print("Function ends")
    return wrapper
@decorator
def func(func_parameter):
    print (func_parameter)

func("Somethinghappening")
