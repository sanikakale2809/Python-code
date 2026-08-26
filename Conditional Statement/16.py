#Customer Bill
custnm=input("Enter the name=")
amt=int(input("Enter the amount="))
if amt>20000:
    print("Discount applied 12%")
    discount=amt*12/100
else:
    print("Discount applied 9%")
    discount=amt*9/100

netbill=amt-discount
print(f"Customer Name={custnm}")
print(f"Purchase Amount={amt}")
print(f"Discount={discount}")
print(f"Net Bill={netbill}")
