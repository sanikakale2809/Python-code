# Create a Student class with a constructor that accepts name and age.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)


s1=Student("Sanika Kale ",22)
s1.display()


# Create an Employee class with name and salary using a constructor.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.salary)

e1=Employee("Bhavesh kale",50000)
e1.display()



# Create a Car class and initialize brand and model using __init__().
class Cars:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(self.brand)
        print(self.model)


c1=Cars("BMW",22)
c1.display()