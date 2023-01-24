str = "I love python programming"

words = str.split(" ") #['I', 'love', 'python', 'programming']
print(words)

rev = words[-1::-1]
print(rev) #['programming', 'python', 'love', 'I']

reversedstring = ' '.join(rev)
print (reversedstring) #programming python love I