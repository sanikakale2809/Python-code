#Nested if conditional statement
shoppingAmt=int(input("Enter your shopping amount="))
if shoppingAmt>=500:
    print("Free Delivery")
    if shoppingAmt>=5000:
        print("Additional 10% Discount")
    else:
        print("No Additional Discount")
else:
    print("RS 50 Delivery charges")