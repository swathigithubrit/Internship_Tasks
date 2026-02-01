# bank_account.py
# -----------------------------------
# This program demonstrates Object-Oriented Programming concepts
# using a real-world Bank Account example.
# Concepts covered:
# - Class & Object
# - Constructor
# - Encapsulation
# - Inheritance
# - Method Overriding (Polymorphism)
# - Multiple objects
# -----------------------------------


class BankAccount:
    """
    Base class representing a generic bank account
    """

    def __init__(self, account_number, holder_name, balance=0):
        """
        Constructor to initialize account details
        """
        self.account_number = account_number
        self.holder_name = holder_name

        # Protected variable (Encapsulation)
        self._balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account
        """
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """
        Method to withdraw money from the account
        """
        if amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        """
        Method to return current balance
        """
        return self._balance

    def display_details(self):
        """
        Display account information
        """
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance        : ₹{self._balance}")


# --------------------------------------------------
# Inheritance Example: Savings Account
# --------------------------------------------------

class SavingsAccount(BankAccount):
    """
    Savings account with minimum balance rule
    """

    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.04):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        """
        Overridden withdraw method
        Enforces minimum balance rule
        """
        minimum_balance = 500

        if self._balance - amount >= minimum_balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn from Savings Account.")
        else:
            print("Withdrawal denied! Minimum balance of ₹500 required.")


# --------------------------------------------------
# Inheritance Example: Current Account
# --------------------------------------------------

class CurrentAccount(BankAccount):
    """
    Current account with overdraft facility
    """

    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=10000):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Overridden withdraw method
        Allows overdraft up to a limit
        """
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"₹{amount} withdrawn using overdraft facility.")
        else:
            print("Overdraft limit exceeded!")


# --------------------------------------------------
# Main Program (Object Creation & Simulation)
# --------------------------------------------------

if __name__ == "__main__":

    print("\n----- Bank Account -----")
    acc1 = BankAccount(101, "Swathi", 5000)
    acc1.display_details()
    acc1.deposit(2000)
    acc1.withdraw(3000)
    print("Final Balance:", acc1.get_balance())

    print("\n----- Savings Account -----")
    acc2 = SavingsAccount(102, "Ravi", 3000)
    acc2.display_details()
    acc2.withdraw(2600)   # Should fail (minimum balance rule)
    acc2.deposit(1000)
    acc2.withdraw(2000)
    print("Final Balance:", acc2.get_balance())

    print("\n----- Current Account -----")
    acc3 = CurrentAccount(103, "Anita", 2000)
    acc3.display_details()
    acc3.withdraw(9000)   # Allowed using overdraft
    acc3.withdraw(5000)   # Exceeds overdraft
    print("Final Balance:", acc3.get_balance())
