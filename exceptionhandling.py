try:
    print("Enter 1st number:")
    x = int(input())
    print("Enter 2nd number:")
    y = int(input())
    if y==0:
        raise Exception("The denminator is Zero")
    print(x/y)
except Exception as e:
    print("The exception is" ,e)
    print("In except block")
else :
    print("In else block") #only when no exception is there , else bloack will be executed
finally:
    print("In finally block") #always this would eb printed even exceptionis there