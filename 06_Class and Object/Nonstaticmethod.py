print("--------------Ex1-------------")

class demo1:             #Class declaration
       # Non Static method
    def m1(self):        #Method declaration
        print("Running method m1")

       # Non Static method
    def square(self,num):
        print(num*num)


#non-static method call
#1: Create Object of class
#2: method call
# objectName=className()
# objectName.methodName()

d1=demo1()                             #1: object creation  -> copy all data from class  into object
d1.m1()                                #2: method calling
d1.square(2)
d1.square(3)



print("------")

class ArithmaticOp:
    def add(self,num1, num2):
        num3=num1+num2
        print(num3)

    def mult(self, num1, num2):
        num3 = num1 * num2
        print(num3)

    def sub(self, num1, num2):
        num3 = num1 - num2
        print(num3)

    def div(self, num1, num2):
        num3 = num1 / num2
        print(num3)

d2=ArithmaticOp()      #contructor
d2.add(7,8)
d2.mult(7,8)
d2.sub(60,40)
d2.div(80,2)
d2.div(50,2)

print("---")
d3=ArithmaticOp()
d3.add(2,7)