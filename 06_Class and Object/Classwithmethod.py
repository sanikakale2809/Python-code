# Calculator
print("------------------Create an object and perform all operations---------------------------")
class Calculator:
    #non static method
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def multiply(self,a,b):
        print(a*b)
    def divide(self,a,b):
        print(a/b)


c1=Calculator()
c1.add(1,2)
c1.sub(3,4)
c1.multiply(3,4)
c1.divide(3,4)
