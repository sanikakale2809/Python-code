#smallest of three numbers
a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
c=int(input("Enter the value of c="))
if (a<b & a<c):
    print(f"{a} is smallest number")
elif(b<a & b<c):
    print(f"{b} is smallest number")
else:
    print(f"{c} is smallest number")
