from abc import ABC, abstractmethod


class Computer():
    @abstractmethod
    def process(self):
        pass

class Laptop():
      def process(self):
          print("I am not in abstract class")
          pass


obj = Computer()
obj.process()
obj1 = Laptop()
obj1.process()
