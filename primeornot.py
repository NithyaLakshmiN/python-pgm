print("Enter a number")
num = int(input())

p=0

for i in range (2,num):
    if num%i==0:
        p=1
        break

if(p==0):
    print("Entered number is prime")
else:
    print("Entered number is not prime")
