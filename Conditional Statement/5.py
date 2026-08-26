#elif conditional statement
ShoppingAmt=int(input("Enter the ShoppingAmt="))
if ShoppingAmt >=20000:
    print("20% discount")
elif ShoppingAmt >=10000:
    print("10% discount")
elif ShoppingAmt >=5000:
    print("5% discount")
else:
    print("no discount")