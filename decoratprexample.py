def outter(x):
    def inner(y):
        return x+y
    return inner

add_five = outter(5)
result = add_five(6)
print(result)