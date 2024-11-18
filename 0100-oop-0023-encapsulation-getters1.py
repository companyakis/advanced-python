class BankAccountInfo:
    def __init__(self, account_holder: str, account_number: int, account_balance: float = 0.0):
        self._account_holder = account_holder
        self._account_number = account_number
        self._account_balance = account_balance
        
    # getter methods
    # properties are NOT public now
    # we need getter methods
    
    def get_account_holder(self):
        return self._account_holder
    
    def get_account_number(self):
        return self._account_number
    
    def get_account_balance(self):
        return self._account_balance
    
# let's open a bank account
    
if __name__ == "__main__":
    
    customer_bilge = BankAccountInfo(
        account_holder="Bilge Kağan",
        account_number=1000001,
        account_balance=8759684.42
    )
    
    # let's print! Possible directly?
    
    # Error!
    
    # "_account_balance" is protected and used outside of the class in which it is declared
    
    print(customer_bilge._account_balance)  
