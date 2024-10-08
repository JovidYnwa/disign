''' An example of a calss that has both data and behivore (methods)
which is not good since letter it will bacome a God class
'''

from dataclasses import dataclass


class BankAccount:
    def __init__(self, account_holder: str, balance: int = 0):
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount: int):
        self.balance -= amount
        return self.balance

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance
    
    def __lt__(self, another_account: "BankAccount")-> bool:
        if self.balance < another_account.balance:
            return True
        return False

''' An example of a datacalss that has both data and behivore (methods)
which is not good since letter it will bacome a God class
'''        
@dataclass
class BankAccountDataClass:
    account_holder: str
    balace: int = 0

    def withdraw(self, amount: int):
        self.balance -= amount
        return self.balance

    def deposit(self, amount: int):
        self.balance += amount
        return self.balance
    
    def __lt__(self, another_account: "BankAccount")-> bool:
        if self.balance < another_account.balance:
            return True
        return False
    
def main():
    account1 = BankAccount("jova", 100)
    account2 = BankAccount("bro", 99)
    account2.deposit(2)
    print(account1 < account2)

if __name__ == "__main__":
    main()