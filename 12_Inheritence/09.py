# Create a parent class Employee with:
# •	name
# •	salary
# Create a child class Manager with:
# •	department
# Display all three values.


class Employee:
    def info(self,name,salary):
        print("Name:",name)
        print("Salary:",salary)

class Manager(Employee):
    def info1(self,department):
        print("department:",department)



m=Manager()
m.info("sanika Kale",60000)
m.info1("Extc")



# Create:
# Animal
#    ↓
# Dog
#    ↓
# Puppy
# Animal should have eat().
# Dog should have bark().
# Puppy should have play().
# Create a Puppy object and call all three methods.



class Animal:
    def eat(self):
        print("eat")

class Dog(Animal):
    def bark(self):
        print("bark")

class Puppy(Dog):
    def play(self):
        print("play")



p=Puppy()
p.eat()
p.play()
p.bark()


# Create a parent class Calculator with methods:
# add()
# subtract()
# Create a child class AdvancedCalculator with:
# multiply()
# divide()
# The child should be able to use all four methods



class Calculator:
    def add(self,a,b):
        print(a+b)

    def sub(self,c,d):
        print(c-d)

class AdvancedCalculator(Calculator):
    def mul(self,e,f):
        print(e * f)

    def div(self,g,h):
        print(g /  h)



c=AdvancedCalculator()
c.add(1,2)
c.sub(8,4)
c.mul(5,6)
c.div(6,2)
