class Student:

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def sum(self, s1, s2, s3):
        s = s1 + s2 + s3
        return s


obj = Student(10, 20, 20)
obj.sum(10,20,30)
print(obj.sum(10,20,30))
