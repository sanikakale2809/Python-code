#  * * * * * * * * * *
#  * * * * * * * * * *
#  * * * * * * * * * *
#  * * * * * * * * * *
#  * * * * * * * * * *


length=int(input("Enter a length:"))
breadth=int(input("Enter a breadth:"))
for i in range(1,breadth+1):
    for j in range(1,length+1):
        print("* ",end="  ")
    print()

