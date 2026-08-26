#elif conditional statement
marks=int(input("Enter the marks="))
if marks>=65:
    print("Distinction")
elif marks>=60 and marks<=65:
    print("1st Class")
elif marks>=50 and marks<=60:
    print("2nd Class")
elif marks>=35 and marks<=50:
   print("3rd Class")
else:
    print("Fail")