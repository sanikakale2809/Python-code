print("--------------------EX1-------------------")
def add(a,b):
    c=a+b
    return c

d=add(45,67)
print(d)


print("---------------------EX2-------------------")
def mul(a,b):
    c=a*b
    return c
d=mul(10,20)
print(d)


print("---------------------EX3-------------------")

def arithmaticOperation(n1, n2):
    add=n1+n2
    mult=n1*n2
    return add,mult

n3,n4=arithmaticOperation(10,20)
print(n3)
print(n4)
print(arithmaticOperation(4,5))
