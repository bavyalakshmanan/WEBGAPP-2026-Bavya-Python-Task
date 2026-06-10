class BankAccount:
    def __init__(self, owner,bank,balance):
        self.owner =  owner
        self._bank = bank
        self.__balance = balance 

    def balance(self):
        return self.__balance
    
    def balance(self,amount):
        if amount < 0: 
         return ("balance cannot be negative")
        self.__balance = amount

    def deposit(self,amount):
       if amount > 0 :
          self.__balance += amount
          return f"Deposited {amount}. Balance: {self.__balance}"

acc = BankAccount("RAJ", "SBI", 5000)

print(acc.balance)
acc.balance = 7000

print(acc.deposit(500))