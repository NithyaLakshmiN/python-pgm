def outter(msg):
    def inner():
        print(msg)
    return inner()

hi = outter("HI")
hello = outter("hello")