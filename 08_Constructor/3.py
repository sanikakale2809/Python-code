# Create a ShoppingCart class where the constructor initializes an empty list of products
class Shopping_cart:
    def __init__(self):
        self.product=[]

cart=Shopping_cart()
print("Products:", cart.product)

s1=Shopping_cart()


# Create a Library class that initializes:
# •	library name
# •	list of books
# Add methods to add and display books.

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Name:", self.library_name)
        print("Books:")

        for book in self.books:
            print(book)


# Create library object
library = Library("City Library")

# Add books
library.add_book("Python Programming")
library.add_book("Java Basics")
library.add_book("Data Structures")

# Display books
library.display_books()


# Create a Student class where the constructor validates that age cannot be negative.

class Student:
    def __init__(self,name,age):
        if age <  0:
            print("Age cannot be negative")
            self.age=0
        else:
            self.age=age

        self.name=name
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)



# Create objects
s1 = Student("Rahul", 20)
s1.display()

s2 = Student("Priya", -5)
s2.display()


# Create a BankAccount class with a constructor and methods:
# deposit()
# withdraw()
# display_balance()

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


# Create account
account = BankAccount("Rahul", 5000)

# Deposit
account.deposit(2000)

# Withdraw
account.withdraw(1000)

# Display balance
account.display_balance()