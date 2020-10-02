"""
Python Bank ATM
- use of methods
- The user needs to be able to make a deposit
- The user needs to be able to pull money out
- The user needs to be able to pay a bill
- The program needs to track the money in the bank
- The user needs to be able to look up their balance
- The program needs to keep running until the user decides to quit the program.
"""


class AccountHolder:
    def __init__(self, account, pin, balance):
        self.account = account
        self.pin = pin
        self.balance = balance

    def account_deposit(self, deposit):
        self.balance = self.balance + deposit
        print(f'You deposited ${deposit}, your new balance is ${self.balance}')
        return self.balance

    def account_withdraw(self, withdraw):
        self.balance = self.balance = withdraw
        print(f'You withdrew ${withdraw}, your new balance is ${self.balance}')
        return self.balance

    def account_billpay(self, company_paid, amount_paid):
        print(f"Check issued to {company_paid} in the amount of ${amount_paid}")
        self.balance = self.balance - amount_paid
        return self.balance

    def account_balance(self):
        print(f"Your balance is {self.balance}")


account_one = AccountHolder(1987, 1234, 1000)


cont_program = True

while cont_program is True:
    if int(input("What is your pin?\n\t")) == account_one.pin:
        navigation = input('What would you like to do? Balance, Deposit, Withdraw, Pay Bill?')[0].lower()
        if navigation == 'b':
            account_one.account_balance()
        elif navigation == 'd':
            account_one.account_deposit(int(input('How much do you want to deposit?\n\t')))
        elif navigation == 'w':
            account_one.account_withdraw(int(input('How much do you want to withdraw?\n\t')))
        elif navigation == 'p':
            account_one.account_billpay(input('Who are we paying?\n\t'), int(input('How much is the bill?\n\t')))
    else:
        print('Wrong pin entered. Goodbye.')
        cont_program = False
