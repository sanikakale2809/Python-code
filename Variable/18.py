# Area of Circle
print("---------------Area of Circle-------------------")
radius=int(input("Enter the radius of circle="))
pi=3.14
area=pi*radius*radius
print(f"Area of circle is {area}")


# Area of rectangle
print("-------------Area of Rectangle-----------------")
length=int(input("Enter the lenghth of rectangle="))
breadth=int(input("Enter the breadth of rectangle="))
area=length*breadth;
print(f"Area of rectangle is {area}")

# Perimeter of Rectangle
print("-------------Perimeter of Rectangle-----------------")
length=int(input("Enter the lenghth of rectangle="))
breadth=int(input("Enter the breadth of rectangle="))
peri=2*(length+breadth);
print(f"Perimeter of rectangle is {peri}")

# Avg of number
print("-------------Avg of number-----------------")
a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
avg=(a+b)/2
print(f"Avg of number is {avg}")

# Calculate BMI
print("-------------Calculate BMI-----------------")
name=input("Enter the name=")
weight=int(input("Enter the weight="))
height=int(input("Enter the height="))
BMI=weight/height**2
print(f"BMI of {name} is {BMI}")

# Simple Interest
print("-------------Simple Interest--------------")
p=int(input("Enter the principal amount="))
r=float(input("Enter the Rate of interest="))
t=int(input("Enter the  time period="))
si=(p*r*t)/100;
print(f"Simple interset is {si}")


# Convert days into years, months.
print("-------------con days to years , months-----------------")
days=int(input("Enter the total no of days="))
years=days/365
month=days/30
print(f"{years}")
print(f"{month}")

#Convert seconds into hours, minutes.
print("---------------con sec to hur and min------------------------")
sec=int(input("Enter the sec="))
hours=sec/3600
min=sec/60
print(f"{hours}")
print(f"{min}")
