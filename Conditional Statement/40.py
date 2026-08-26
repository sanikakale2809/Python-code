#Triangle Type
a=int(input("Enter a of triangle="))
b=int(input("Enter b of triangle="))
c=int(input("Enter c of triangle="))
if a == b == c:
    print("The triangle is Equilateral")
elif a == b or b== c or c==a:
    print("The triangle is Isoceles")
elif a != b and b != c and a != c:
    print("The triangle is Scalene")