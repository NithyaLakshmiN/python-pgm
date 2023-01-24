mylist = ["gautham","kaarthik","gautham"]
n=2
count = 0
for i in range(0,len(mylist)):
    if mylist[i] == "gautham":
        count += 1
        if count == 2:
            del mylist[i]
            newlist = mylist
            print(newlist)