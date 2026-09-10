print("-----Ex1:  Examples of Modules (APR1)-----")

# Module1: Operations

# Syntax:
# import moduleName

# moduleName.fn()            #fn calling

# objName=moduleName.className()          #calling non-static method
# objName.methodName()

#moduleName.className.methodName()        #calling static method


import Calculator1
import Calculator2

print("------contents of Calculator1 module-----")
Calculator1.add(2,3)       #fn calling
Calculator1.add(7,8)
Calculator1.mult(4,5)

d1=Calculator1.Demo1()                #object creation
d1.m1()                               #method calling
d1.m2()
d1.m2()

Calculator1.Demo1.m3()             #calling static method
Calculator1.Demo1.m3()


print("------contents of Calculator2 module-----")


Calculator2.div(6,2)             #fn calling
Calculator2.sub(90,40)

d2=Calculator2.Demo2()                       #object creation
d2.m4()                                      #non-static method calling

Calculator2.Demo2.m5()                      #static method calling
