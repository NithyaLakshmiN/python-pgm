list1 = ["India","Pune","Kolkatta","Blr","Chennai","Rajasthan"]
list2 = ["UK","USA","UAE","Africa","Asia","Antarctica"]
s1=map(list1,list2)

s = zip(list1,list2) #This would return an object combimg both the list
print(list(s)) #

for x,y in zip(list1,list2):
    print(x,y)