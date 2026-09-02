# Find the sum of numbers from 1 to N
N=int(input("Enter N: "))
total = 0
for i in range(1, N+1):
    total = total + i
print("Sum =", total)