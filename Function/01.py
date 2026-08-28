# Create a simple function
print("--------------Ex1-----------")
def greet():
    print("Hello, Welcome to python")

greet()


#Function with no arguments
print("--------------Ex2-----------")
def fun():
    print("Sanika kale","Amaravati")

fun()


#Function with one argument
print("--------------Ex3-----------")
def greet(name):
    print("Hello,",name)

greet("sanika")


#Add two numbers
print("--------------Ex4-----------")
def add(a,b):
    return a+b

print(add(3,4))


#Check even or odd
print("--------------Ex5-----------")
def num(a):
    if a % 2 ==0:
        print("a is even number")
    else:
        print("a is odd number")
num(5)
num(6)


#Subtract two numbers
print("--------------Ex6-----------")
def sub(a,b):
    c=a-b
    return c
print(sub(3,4))


#Find square
print("--------------Ex7-----------")
def square(a):
    return a*a
print(square(4))


# cube
print("--------------Ex8-----------")
def cube(a):
    return a*a*a
print(cube(4))

# Maximum
print("--------------Ex9-----------")
def max(a,b):
    if a >b :
        return a
    else:
        return b
print(max(4,5))

#Positive, negative or zero
print("--------------Ex10-----------")
def num(a):
    if a > 0:
        print("a is positive")
    elif a < 0:
        print("a is negative")
    else:
        print("a is zero")
num(5)
num(0)
num(-9)

