#Triangle Validity
a=int(input("Enter side1 of triangle="))
b=int(input("Enter side2 of triangle="))
c=int(input("Enter side3 of triangle="))
if a+b >b and a+c >c and b+c >c:
    print("This side is form a triangle.")
else:
    print("This side is not form a triangle.")