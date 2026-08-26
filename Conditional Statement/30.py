# Divisibility check
num=int(input("Enter a number="))
if num%5==0:
    print(f"{num} is divisible by 5")
elif num%3==0:
    print(f"{num} is divisible by 3")
elif num%3==0 and num%5==0:
    print(f"{num} is divisible by 5 and 3")
else:
    print(f"{num} is neither divisible by 3 nor 5")