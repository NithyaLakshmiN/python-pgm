# def is_even(n):
#     return n % 2 == 0 This can be defined as shown in below lambda function
# def update(n):
#     return n + 2

# def add_all(a,b):
#     return(a+b)

from functools import reduce

nums = [2, 8, 10, 4, 3, 9, 5, 6]

evens = list(filter(lambda n: n % 2 == 0, nums))

doubles = list(map(lambda n: n + 2, evens))

sum = reduce(lambda  a,b : a+b,doubles)

print(evens)  # prints all the ven numbers
print(doubles)
print(sum)
