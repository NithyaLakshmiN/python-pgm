class Rateofinterest:
    interest = 8 #class variable

    def __init__(self,name , loan):
        self.loan = loan #instance variable
        self.name =  name #instance variable

    def calroi(self):
        print("Totalinterest" , self.loan * self.interest)

obj = Rateofinterest("Nithya",70)
#Rateofinterest.interest =9
obj.calroi()

#instance varible belongs to that paricular instance and defne in init method
#Class variable definedin class and can be access across
#Rateofinterest.interest =9 - when this value is to be passed , refer it with class name as Rateofinterest.interest
#self refers to that particular instance
