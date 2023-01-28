n = int(input("enter a number: "))
factors = []
for i in range(1,n+1):
    if n % i == 0:
        factors.append(i)
print(f"the factors of the number {n} are {factors}")