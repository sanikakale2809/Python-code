#student result
name=input("Enter the name of student=")
marks=int(input("Enter the marks="))
if marks>35:
   print("congratulations")
   print(f"{name},you are pass")
else:
   print("sorry")
   print(f"{name},you are fail")