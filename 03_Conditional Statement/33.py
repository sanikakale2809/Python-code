# Three-Digit Number
#using range
num=int(input("Enter the number ="))
if num > 99 and num < 1000:
    print(f"{num} is a three digit number")
else:
    (print(f"{num} is not  three digit number"))


#using abs() it cover negative number also
num = int(input("Enter a number: "))
if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")



