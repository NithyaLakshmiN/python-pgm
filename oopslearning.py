class Computer:

    def __init__(self, cpu, ram, school, four):
        self.cpu = cpu
        self.ram = ram
        self.school = school
        self.grade = four

    def config(self):
        print("config is", self.cpu, self.ram, self.school, self.grade)

    def nithya(self):
        print("I am in pass", self.cpu, self.school, self.grade)

    def gautham(self):
        print("I am in Gautham", self.school, self.grade)


com1 = Computer('ryan', 16, "carmel", 4)
com2 = Computer('lolan', 20, "carmel", 4)
com3 = Computer('lolan2323', 2023213, "carmel", 4)
com4 = Computer('lolan2324', 2023214, "carmel", 4)

com1.config()
com2.config()
com3.nithya()
com4.gautham()
