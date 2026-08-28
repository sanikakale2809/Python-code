#Right Angle Triangle
# 1 Method
a=int(input("Enter a of triangle="))
b=int(input("Enter b of triangle="))
c=int(input("Enter c of triangle="))
if a >=b and a>=c:
    if b*b + c*c == a*a:
        print("It is Right-Angled Triangle")
    else:
        print("It is not Right-Angled Triangle")
elif b>=a and b>=c:
    if a*a + c*c == b*b:
        print("It is Right-Angled Triangle")
    else:
        print("It is not Right-Angled Triangle")
elif c>=a and c>=b:
    if a*a + b*b == c:
        print("It is Right-Angled Triangle")
    else:
        print("It is not Right-Angled Triangle")



#2 Method

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

sides = sorted([a, b, c])

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Right-angled triangle")
else:
    print("Not a right-angled triangle")