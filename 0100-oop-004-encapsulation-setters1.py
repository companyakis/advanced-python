class BankAccountInfo:
    def __init__(self, account_holder: str, account_number: str, account_balance: float = 0.0):
        self._account_holder = account_holder
        self._account_number = account_number
        self._account_balance = account_balance
        
    # getter methods
    def get_account_holder(self):
        return self._account_holder
    
    def get_account_number(self):
        return self._account_number
    
    def get_account_balance(self):
        return self._account_balance
    
    # setter methods
    def set_account_holder(self, ah: str):
        self._account_holder = ah
    
    def set_account_number(self, an: str):
        self._account_number = an
    
    def set_account_balance(self, ab: float):
        if ab >= 0.0:
            self._account_balance = ab
        else:
            print("Account balance can't be negative!")   
    
    
if __name__ == "__main__":
    
    customer_bilge = BankAccountInfo(
        account_holder="Bilge Kağan",
        account_number="1000001",
        account_balance=8759684.42
    )
    
