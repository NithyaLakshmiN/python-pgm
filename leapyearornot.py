print("Enter year")
y= int(input())

if y%4==0 and y%100!=0 :
    print("This is leap year")
elif y%400==0 :
    print("This is leap year")
else :
    print("This is not a leap year")