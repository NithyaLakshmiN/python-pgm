class car():
    def __init__(self, cn, cmy, cp):
        self.cn = cn
        self.cmy = cmy
        self.cp = cp


class SuperCar(car):
    pass


obj1 = SuperCar("Honda", 2018, 56)
obj2 = car("Tata", 2017, 86)
print(help(obj1))
