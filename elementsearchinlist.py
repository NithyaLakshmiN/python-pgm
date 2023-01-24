mylist = [8,7,6,5,4,3,2,1]
flag= 0
ele = 10
for i in mylist:
    if ele==i:
        print("element found")
        flag=1
        break
if(flag==0):
    print("element not found")