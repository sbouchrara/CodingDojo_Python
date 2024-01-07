# Core Assignment - Bank Account
# Programmer - Bouchrara Saiffallah
class BankAccount:
    all_accounts = []

    def __init__(self, p_int_rate, p_balance) :
        self.int_rate   = p_int_rate
        self.balance    = p_balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def all_bank_account(cls):
        print("-"*40)
        for account in cls.all_accounts:
            print(account.balance)
    

    def deposit(self, p_amount) :
        # increases the account balance by the given amount
        self.balance += p_amount
        return self

    def withdraw(self, p_amount) :
        # decreases the account balance by the given amount if there are sufficient funds; 
        # if there is not enough money, 
        #   ==> print a message "Insufficient funds: 
        #   ==> Charging a $5 fee" and deduct $5
        if p_amount < self.balance:
            self.balance -= p_amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self


    def display_account_info(self) :
        # print to the console: eg. "Balance: $100"
        print(f"balance: ${self.balance}")

    def yield_interest(self) :
        # increases the account balance by 
        # the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0 :
            self.balance += self.balance * self.int_rate
        return self

account_1 = BankAccount(0.0399,5000)
account_2 = BankAccount(0.0449,15000)

account_1.display_account_info()
account_1.deposit(1000).deposit(1500).deposit(2000).withdraw(10000).yield_interest().display_account_info()

account_2.display_account_info()
account_2.deposit(500).deposit(1000).withdraw(3000).withdraw(4000).withdraw(1000).withdraw(2500).yield_interest().display_account_info()

BankAccount.all_bank_account()