# 	Create a BankAccount class with:
# 	account number
# 	account holder
# 	balance
# Initialize all three using a constructor.

class Bank_Account:
    def __init__(self,account_number,account_holder,balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def display(self):
        print("Account number =",self.account_number)
        print("Account holder =",self.account_holder)
        print("Balance =",self.balance)

b1=Bank_Account(123456789,"sanika kale",50000)
b1.display()


# Create a Product class with name, price, and quantity. Calculate total price
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def display(self):
        print("Product name =",self.name)
        print("Product price =",self.price)
        print("Product quantity =",self.quantity)
        print("Total Price =",self.price*self.quantity)


p1=Product("Body Lotion",800,10)
p1.display()


# Create a Rectangle class where the constructor accepts length and width. Find area.

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        print("Rectangle length =",self.length)
        print("Rectangle width =",self.width)
        print("Area=",self.length * self.width)


R1=Rectangle(10,20)
R1.display()


# Create a Student class with name, marks1, marks2, and marks3. Calculate average marks.

class Student:
    def __init__(self,name,Eng,Mar,Hin):
        self.name=name
        self.Eng=Eng
        self.Mar=Mar
        self.Hin=Hin
    def display(self):
        print("Student name =",self.name)
        print("Student Eng =",self.Eng)
        print("Student Mar  =",self.Mar)
        print("Student Hin =",self.Hin)
        print("Average marks =",(self.Eng+self.Mar+self.Hin)/3)


s1=Student("Sanika kale",90,98,97)
s1.display()


# Create an Employee class with name, salary, and department. Display employee details.
class Employee:
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept
    def display(self):
        print("Employee name =",self.name)
        print("Employee salary =",self.salary)
        print("Employee dept =",self.dept)


e1=Employee("sanika kale",80000,"atomation")
e1.display()


# Create a Mobile class with default values for brand and price.
class Mobile:
    def __init__(self, brand="Samsung", price=20000):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


# Object using default values
m1 = Mobile()
m1.display()

# Create a class where the constructor has both default and parameterized arguments.
class Mobile:
    def __init__(self, brand, price=20000):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


# Parameterized brand, default price
m1 = Mobile("Samsung")
m1.display()

# Both values provided
m2 = Mobile("iPhone", 50000)
m2.display()