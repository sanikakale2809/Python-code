#Triangle validity
a=int(input("Enter side1 of triangle="))
b=int(input("Enter side2 of triangle="))
c=int(input("Enter side3 of triangle="))
if a+b>c and a+c>b and b+c>a:
    print("This side form a triangle")
else:
    print("This side can't form a triangle")