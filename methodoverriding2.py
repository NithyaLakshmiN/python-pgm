class Student:

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def sum(self, s1=None, s2=None, s3=None):
        s = 0
        if s1 is not None and s2 is not None and s3 is not None:
            s = s1 + s2 + s3
        elif s1 is not None and s2 is not None:
            s = s1 + s2
        else:
            s = s1
        return s


obj = Student(10, 20, 20)
obj.sum(10, 20, 30)
print(obj.sum(10, 20))
print(obj.sum(10, 20,30))
print(obj.sum(10,))
