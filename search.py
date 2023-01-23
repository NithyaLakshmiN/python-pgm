import self as self


class search:
    def linearsearch(self):
        mylist = []
        num = int(input("Enter the list size"))
        i = 0
        flag = False
        for n in range(num):
            numbers = int(input("Enter the array of %d element :- " % n))
            mylist.append(numbers)
        x = int(input("Enter the number to be searched in the list"))
        while i < len(mylist):
            if mylist[i] == x:
                flag = True
                break
            i = i + 1

        if flag == 1:
            print(f"{x} is found at the index of {i}")
        else:
            print(f"{x} is not available in the list")

    def binarysearch(self):
        mylist = []
        num = int(input("Enter the list size"))
        for n in range(num):
            numbers = int(input("Enter the array of %d element :- " % n))
            mylist.append(numbers)
        x = int(input("Enter the number to be searched in the list"))
        #print(mylist.sort())
        first = 0
        last = num-1
        middle= (first + last) / 2
        middle = int(middle)
        while first <= last:
            if mylist[middle] < x:
                first = middle + 1
            elif mylist[middle] == x:
                print(f"The number {x} is at the position: {first}")
                break
            else:
                last = middle - 1
            middle = (first + last) / 2
            middle = int(middle)
        if first > last:
            print(f"The Number {x} is not Found in the List")


s = search()
# s.linearsearch()
s.binarysearch()
