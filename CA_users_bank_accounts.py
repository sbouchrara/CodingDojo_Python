# Core Assignment - Users with Bank Accounts

class BankAccount:
    all_accounts = []

    def __init__(self, p_int_rate, p_balance, p_accountno) :
        self.int_rate   = p_int_rate
        self.balance    = p_balance
        self.accountno  = p_accountno
        BankAccount.all_accounts.append(self)

    @classmethod
    def all_bank_account(cls):
        print("-"*40)
        for account in cls.all_accounts:
            print(account.balance)

    @classmethod
    def search_account(cls,accountnumber):
        for account in cls.all_accounts :
            if account.accountno == accountnumber:
                print(account.accountno)

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
        print(f"balance: ${self.balance}")

    def yield_interest(self) :
        # increases the account balance by 
        # the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0 :
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, p_int_rate,p_balance,p_accountno,p_name,p_email):
        self.name   = p_name
        self.email  = p_email
        self.account = BankAccount(p_int_rate,p_balance,p_accountno)
        

    def make_deposit(self, amount,user_acc):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name} Email: {self.email} Account Number: {self.account.accountno} Balance: ${self.account.balance} Interest rate: {self.account.int_rate}")

account_1 = User(0.03,4000,55177747,"alain","alain@toto.com")
account_2 = User(0.029,1000,10786556,"alain","alain@toto.com")
account_1.display_user_balance()
account_2.display_user_balance()

op_stat = input("Please introduce 1 for deposit and 2 for withdrawal operation: ")
if (op_stat == "1") or (op_stat == "2") :
    acc_no = input('introduce please your account number')
    if acc_no != " ":
        if op_stat == "1":
            account_1.make_deposit(3000,acc_no).display_user_balance()
        elif op_stat == "2":
            account_1.make_withdrawal(500).display_user_balance()
    else:
        print("Account number should be introduced")
else:
    print('status not indicated')