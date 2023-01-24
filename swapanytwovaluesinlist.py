mylist = [8,7,6,5,4,3,2,1]
print(mylist)
pos1,pos2 =1,3
mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)
mylist[::1]=mylist[::-1]
print(mylist)