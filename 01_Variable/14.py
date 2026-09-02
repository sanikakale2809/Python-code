#swap two number without using third variable
a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
a=a+b
b=a-b
a=a-b
print(f"a after swap {a}")
print(f"b after swap {b}")
