#nested if conditional statement
PEM=int(input("Enter PEM="))
if PEM >= 250:
    print("Selected in prelim exam")
    print("Preparing for main exam")
    if PEM >=500:
        print("Selected in Mains exam")
    else:
        print("Rejected from mains exam")
else:
    print("Rejected from prelim exam")
