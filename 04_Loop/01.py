# Print numbers 1 to 10
for i in range(1,11):
    print(i)

#Print number 10 to 1
for i in range(10,0,-1):
    print(i)

# Print even number from 1 to 20
for i in range(2,21,2):
    print(i)

# Print odd number from 1 to 20
for i in range(1, 20, 2):
    print(i)

# Print numbers 1 to 100
for i in range(1,101):
    print(i)

#Print the multiplication table of 5
for i in range(1,11):
    print(i*5)

# Print the multiplication table of a user-given number
n=int(input("Enter a number: "))
for i in range(1,11):
    print(i*n)

# Print each character of a string
for ch in 'Sanika':
    print(ch)


# Find the sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total = total + i
print("Sum =", total)


#Find the sum of even numbers from 1 to 50
total = 0

for i in range(1, 51):
    if i % 2 == 0:
        total = total + i

print("Sum of even numbers =", total)
