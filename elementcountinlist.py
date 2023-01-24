mylist = [4,5,6,7,8,9.4,7,8,6]
x = 8
count= 0
for i in mylist:
    if(i==x):
        count=count+1
print("{} has occured {} times".format(x,count) )