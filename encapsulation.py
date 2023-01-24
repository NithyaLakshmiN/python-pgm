class car :
    def __init__(self):
        self.__updatesoftware()  #This has __ which is a provate method and cannot be called outside class

    def drive(self):
        print("driving")

    def __updatesoftware(self):
        print("updating software")

obj1 = car()
obj1.drive()
#obj1.__updatesoftware()  #This is not possible cos this is outside the class
print(help(obj1.drive()))