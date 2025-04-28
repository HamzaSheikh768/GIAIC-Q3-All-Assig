# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
# that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Default Bank"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

#____________________________ Example usage
b1 = Bank("Alice")
b2 = Bank("Bob")
print(f"Before: {b1.bank_name}, {b2.bank_name}")
Bank.change_bank_name("New Bank")
print(f"After: {b1.bank_name}, {b2.bank_name}")