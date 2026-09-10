# Importing the Employee class from employee.py
from Employee import Employee
from Bank import BankAccount

def main():
    # Creating three employee objects
    emp1 = Employee("Alice Smith", "E001", "Human Resources")
    emp2 = Employee("Bob Jones", "E002", "Engineering")
    emp3 = Employee("Charlie Brown", "E003", "Marketing")

    # Displaying the details of each employee
    print("--- Employee Records ---")
    emp1.display_info()
    emp2.display_info()
    emp3.display_info()


    b1 = BankAccount("Rahul", 5000)
    b1.deposit(4000)
    b1.withdraw(400)
    b1.display_balance()

if __name__ == "__main__":
    main()
