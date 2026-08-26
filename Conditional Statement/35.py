#Simple ATM
balance = 10000
withdrawal = int(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount")

elif withdrawal > balance:
    print("Insufficient balance")

else:
    balance = balance - withdrawal
    print("Withdrawal successful")
    print("Remaining balance:", balance)