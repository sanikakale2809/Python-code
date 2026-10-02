# *
# * *
# * * *
# * * * *


print("---------------1st apr------------")
n=int(input("Enter the number:"))
for i in range(1,n+1):
    print('* '* i )
print( )



#  *
#  **
#  ***
#  ****

print("---------------2ed apr------------")
n=int(input("Enter the number:"))
star=1
for i in range(n):
    for j in range(star):
        print("*",end="")
    print()
    star +=1


# *
# ***
# *****
# *******

print("---------------3rd apr------------")
n=int(input("Enter the number:"))
star = 1
for i in range(n):
    for j in range(star):
        print("*", end="")
    print()
    star += 2
