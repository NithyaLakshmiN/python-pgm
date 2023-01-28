from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self,name,id,marks):
        self.name= name
        self.id = id
        self.marks = marks

    def __studentrecord(self):
        print("Student record listed as",self.name ,self.id,self.marks)
        print("Student reocrds printed successfully")

    @abstractmethod
    def studentrecord(self):
        pass

class superstudent(Student) :
    pass



obj = Student("Gautham",67,9.5)
#obj.__studentrecord()
#obj1 = superstudent("Kaarthik",70,10)

#print(obj1.marks)
print(help(obj.studentrecord()))