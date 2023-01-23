import cmath
print("general form : ax**2 + bx + c")
a = int(input("enter a (a != 0): "))
b = int(input("enter b: "))
c = int(input("enter c: "))
print("\n")
print(f"the results for {a}x**2 + {b}x + {c} = 0 are: \n")

d = b**2 - 4*a*c
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

if d > 0:
    print("two distinct real roots")
elif d == 0:
    print("two equal real roots")
else:
    print("two complex roots")
print(f"the two solutions are {sol1} and {sol2}")
