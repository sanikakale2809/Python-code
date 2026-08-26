nm=input("Enter the name of student=")
marks=int(input("Enter the marks of student="))
if(marks >=90):
    print(f"{nm}=A")
elif(marks >=80 ):
    print(f"{nm}=B")
elif(marks >=70 ):
    print(f"{nm}=C")
elif(marks >=60 ):
    print(f"{nm}=D")
else:
    print(f"{nm} is fail.")
