# Bill
custnm=input("Enter the name of customer=")
amount=float(input("Enter the purchase amount="))
discount=amount*10/100
netamount=amount-discount
print(f"Customer Name= {custnm}")
print(f"Purchse Amount={amount}")
print(f"Discount={discount}")
print(f"Net Amount={netamount}")