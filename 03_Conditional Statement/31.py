#Take temperature and print
tem=int(input("Enter the temperature="))
if tem< 10:
    print("very cold")
elif tem > 10 and tem < 20:
    print("cold")
elif tem > 20 and tem < 30:
    print("Normal")
elif tem > 30 and tem < 40:
    print("Hot")
else:
    print("very hot")