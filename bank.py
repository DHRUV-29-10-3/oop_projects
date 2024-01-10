class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self,deposit_amount):
        self.balance += deposit_amount


    def Withdrawal(self,withdraw_amount):
        self.balance -= withdraw_amount

    def bankFees(self):
        intrest = 5
        self.balance -= (self.balance*intrest)/100
        print(self.balance)

    def display(self):
        print('Account Number :',self.accountNumber)
        print('Account Name :',self.name)
        print(f'Account Balanc : {self.balance} $')

newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()