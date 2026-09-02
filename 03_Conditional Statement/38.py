#Calculate electricity bill based on units:
#0–100 units     → ₹5/unit
#101–200 units   → ₹7/unit
#201–300 units   → ₹10/unit
#Above 300       → ₹15/unit

unit=int(input("Enter a unit="))
if unit > 0 and unit <=100:
    print("5 ru unit is applied")
    unit_Rate=5
elif unit > 100 and unit <=200:
    print("7 ru unit is applied")
    unit_Rate=7
elif unit > 200 and unit <=300:
    print("10 ru unit is applied")
    unit_Rate=10
elif unit > 300:
    print("15 ru unit is applied")
    unit_Rate=15

electricity_bill=unit*unit_Rate
print(electricity_bill)