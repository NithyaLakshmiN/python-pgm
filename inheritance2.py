class car():
    def __init__(self, cn, cym, cp):
        self.cn = cn
        self.cp = cp
        self.cym = cym


class SuperCar(car):
    def __init__(self, cn, cym, cp, cc):
        super(SuperCar, self).__init__(cn, cym, cp)
        self.cc = cc


obj1 = SuperCar("Honda", 2016, 400000, 89)
print(obj1.__dict__)
obj2 = car("Tata", 2017, 40078000)
print(obj2.__dict__)
obj3 = SuperCar("Honda", 2016, 400000, 90)
print(obj3.__dict__)
