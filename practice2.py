mylist =[]
str1 = "123hewrdllo"
mylist[:0]=str1
#print(mylist)
mylist2=[]
for i in mylist:
    if i == 'h' or i == 'e' or i == 'l' or i == 'o':
        mylist2.append(i)
print(mylist2)

listToStr = ' '.join(map(str, mylist2))

print(listToStr)