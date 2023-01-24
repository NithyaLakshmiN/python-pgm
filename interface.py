from abc import ABC, abstractmethod


class myinterface(ABC):
    @abstractmethod
    def func1(self):
        pass


class myclass(myinterface):
    def func1(self):
        print("I am overrided")


obj = myclass()
obj.func1()
