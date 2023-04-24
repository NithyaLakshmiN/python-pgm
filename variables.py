# # import keyword
# import time
# # username = 'Nithya'
# # print(username)
# # print(type(username))
# # username = 10
# # print(username)
# # print(type(username))
# # username = 10.0
# # print(username)
# # print(type(username))
# # print(id(username))
# # _A = 2
# # print(_A)
# # A0 = 20
# # print(A0)
# # list = keyword.kwlist
# # print(list)
# # x =15
# # y=10
# # print(x+y)
# # print(x-y)
# # print(x/y)
# # print(x%y)
# # print(x**y)
# # print(x==y)
# # print(x//y)
# # print(x!=y)
# # print(x+2)
# # print(x-4)
# # print(x>y)
# # print(x<y)
# # print(x<=y)
# # print(x>=y)
# # print(x>y and x==30)
# # print(x>y or x==30)
#
# x= lambda y ,z: y*z
# print(x(4,5))
# c=''' jadjafhdjfdjfhdjfh dfjdkfhdjfhdsjfh ajdfhjdshfsdjfhdsjfh ajhfjadfhdf
# kjdfkdjfkdsjf sdjgksjgkfsgjfkg
# kdfjkdsjfkdsf
# sdfjdsfhd
# dkfjkdfdks
# dfjdsf'''
# print(c)
# g= 9283921839
# f = str(g)
# print(f.find("9"))
# f.isdigit()
# print(c.upper())
# print (c.count("J",10,20))
# # string_test = "Nithya Lakshmi"
# # print(string_test[1:-1])
# # print(string_test[::-1])
# # # print(string_test[-7:-1])
# # # i = "name,age,city"
# # # #print(i[0:i.index(",")])
# # #
# # # #print(i.find("age"))
# # #
# # # print(i[1:-1])
# #
# # string_test = ['interview' , 'test',40,30,40]
# # print(type(string_test))
# # print(string_test[1])
# # string_test.insert(0,"I am added")
# # print(string_test)
# # string_test.append("I am appended")
# # print(string_test)
# # string_test.remove("I am appended")
# # print(string_test)
# # string_test.pop(0)
# # print(string_test)
# # string_test.pop()
# # print(string_test)
# # print(string_test.index('interview'))
# # print(string_test.count('int'))
# # string_test [0] = 'interviewdone'
# # print(string_test)
# # string_test1 = ['interviews' , 'tests',400,300,400]
# # mylist = string_test.extend(string_test1)
# # string_test.reverse()
# # print(string_test)
# # for i in string_test:
# #     print(i)
#
# myset = {"Nithya",1,2,"Lakshmi","Lakshmi"}
# print(myset)
# myset.add(6)
# print(myset)
# myset.remove(6)
# print(myset)
# myset.pop()
# print(myset)
# myset2 = {"1","Delhi","4",6,7,8,1, 2, 6, 'Lakshmi', 'Nithya' }
# print(myset2)
# myset3=myset.union(myset2)
# print(myset3)
# myset4=myset2.copy()
# print(myset4)
# myset5 =myset3.difference(myset)
# print(myset5)
# myset5.issubset(myset)

# mytuple = ('4', 1, '1', 2, 'Nithya', 6, 7, 8, 'Delhi', 'Lakshmi','Nithya', 2, 1, 'Lakshmi')
# print(mytuple)
# print(mytuple.count(1))
# print(len(mytuple))

# mytuple = ([1,9],[1,2])
# mylist = list (mytuple)
# print(mylist)
# print(mylist[0][1])

mydict ={"name":"Nithya" , "Class":"Four" , "School":"Carmel" ,"School":"Carmel" }
print(mydict["School"])
print(mydict.get("name"))
print(mydict.values())
mydict['prod']="lucky"
print(mydict)
mydict.pop("Class")
print(mydict)