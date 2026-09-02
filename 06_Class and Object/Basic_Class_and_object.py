# Student Class
print("----------------print name, age , course------------------")


class Class:

    def student1(self, name, age, course):
        print("Student name : ", name)
        print("Student age : ", age)
        print("Student course : ", course)

    def student2(name, age, course):
        print("Student name : ", name)
        print("Student age : ", age)
        print("Student course : ", course)


c1 = Class()
c1.student1("Sanika ", 22, "Extc")

Class.student2("Sanika", 22, "Extc")


# Employee Class
print("------------------------Name,Salary--------------------------")
class Employee:

    def employee1(self, name, salary):
        print("Employee name : ", name)
        print("Employee salary : ", salary)

    def employee2(name, salary):
        print("Employee name : ", name)
        print("Employee salary : ", salary)

e1=Employee()
e1.employee1("Sanika ", 2200000)

Employee.employee2("sanika",300000)


# Car class
print("---------------------Brand,Model,Price---------------------")
class Cars:
    def car1(self,Brand,Model,Price):
        print("Brand : ", Brand)
        print("Model : ", Model)
        print("Price : ", Price)

    def car2(Brand,Model,Price):
        print("Brand : ", Brand)
        print("Model : ", Model)
        print("Price : ", Price)


a1=Cars()
a1.car1("BMW", 4, "12000000")

Cars.car2("BMW", 4, "12000000")

# Mobile Class
print("------------------Brand,Price,color--------------------")
class Mobile:
    def mobile1(self,Brand,Model,Price):
        print("Brand : ", Brand)
        print("Model : ", Model)
        print("Price : ", Price)

    def mobile2(Brand,Model,Price):
        print("Brand : ", Brand)
        print("Model : ", Model)
        print("Price : ", Price)


m1=Mobile()
m1.mobile1("nokia", 13, "12000")
Mobile.mobile2("nokia", 13, "12000")

# Bank Account
print("---------------------Accountholder,balance----------------------")

class Account:

    def account1(self,Account_holder,Balance):
        print("Account holder : ", Account_holder)
        print("Balance : ", Balance)

    def account2(Account_holder,Balance):
        print("Account holder : ", Account_holder)
        print("Balance : ", Balance)

A1=Account()
A1.account1("Sanika Kale",1200000)

Account.account2("Sanika Kale",1200000)