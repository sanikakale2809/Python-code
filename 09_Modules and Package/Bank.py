# Create a BankAccount class with a constructor and methods:
# deposit()
# withdraw()
# display_balance()

# create a BankAccount class
class BankAccount:
    # create a constructor
    def __init__(self,Account_holder,Balance):
        self.Account_holder = Account_holder
        self.Balance = Balance

    def deposit(self,Amount):
        self.Balance += Amount
        print("Deposit Amount:",Amount)

    def withdraw(self,Amount):
        if Amount <= self.Balance:
            self.Balance -= Amount
            print("Withdrawn:", Amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
            print("Account Holder:", self.Account_holder)
            print("Balance:", self.Balance)

