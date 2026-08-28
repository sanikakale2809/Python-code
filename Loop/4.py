# Find the factorial of a number
N=int(input("Enter the : "))
fac = 1
for i in range(1, N+1):
    fac = fac * i
print("factorial =", fac)
