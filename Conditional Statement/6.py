#elif conditional statement
shoppingAmt=int(input("Enter shoppingAmt="))
if shoppingAmt>=20000:
    print("20% discount")
elif (shoppingAmt>=10000 and shoppingAmt<20000):
    print("10% discount")
elif (shoppingAmt>=5000 and shoppingAmt<10000):
    print("5% discount")
else:
    print("no discount")
