class Atm:
    def __init__(self):
        self.pin = 0
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input("""How can i help you?\n1) Press 1 to create pin.\n2) Press 2 to change the pin.\n3) Press 3 to check the balance.\n4) Press 4 to withdraw the money.\n""")

        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.rechanging_pin()
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = int(input('Enter the pin:'))
        self.pin = user_pin

        user_balance = int(input('Enter the balance:'))
        self.balance = user_balance

        print('Pin created sucessfully')

        self.menu()

    def check_balance(self):
        old_pin = int(input('Enter the pin:'))
        if old_pin == self.pin:
            print('Your current balance is:',self.balance)

        else:
            print('Please enter correct pin')

        self.menu()


    def rechanging_pin(self):
        old_pin = int(input('Enter the old pin:'))
        if old_pin == self.pin:
            new_pin = int(input('Enter the new pin:'))
            self.pin = new_pin
            print('Pin changed sucessfully')

        else:
            print('Please enter correct pin')

        self.menu()

    def withdraw(self):
        old_pin = int(input('Enter the pin:'))
        if old_pin == self.pin:
            withdraw_amt = int(input('Enter the money you want to withdraw:'))
            self.balance -= withdraw_amt
            print('Your current balance is:$',self.balance)

        else:
            print('Please enter correct pin')

        self.menu()

object = Atm()

