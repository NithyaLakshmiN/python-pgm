class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is", self.cpu, self.ram)


com1 = Computer('ryan', 16)
com2 = Computer('lolan', 20)
com1.config()
com2.config()
