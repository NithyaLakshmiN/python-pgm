class test ():
    def __init__(self):
        self.var = 10
        self._var1 = 20 #This is private variable
        self.__var2 = 30 #This is private variable

      #in getter method we can get the value of the private variable

    def get_var2(self):
        return self.__var2

    # in setter method we can set the value of the private variable
    def setter_var2(self,num):
        self.__var2 =num


    def func(self):
        print(self.var)
        print(self._var1)
        print(self.__var2)

    def _func(self):    #This is private method,since it has single_
        print(self.var)
        print(self._var1)
        print(self.__var2)

obj = test()
obj.func() #here only func wud be displayed on listing , cos __func is private and cannot be called outside class , and this sort of prvate can be used to define passwords and usernames in out prgrams so external user cannot change values
print(obj.get_var2())
obj.setter_var2(22)
print(obj.get_var2())
