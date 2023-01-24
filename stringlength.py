# str = "Gautham Kaarthik"
# count =1
#
# for i in str:
#     count = count+1
# print("Given String length is", count)

#Findng string length using count and joint

str = "Gautham Kaarthik"
randomstr ='X'

print((randomstr).join(str)) #GXaXuXtXhXaXmX XKXaXaXrXtXhXiXk
print((randomstr).join(str).count(randomstr)) #15
print((randomstr).join(str).count(randomstr)+1)
