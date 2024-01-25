import BankAccount


# I hope for the most part, this class is straight forward to you. I do not think I did anything fancy which really
# calls for comments in it

class Bank:
    _accounts = []
    _account_number = 0

    def __init__(self, name):
        self.name = name

    def create_account(self):
        Bank._account_number += 1
        new_account = BankAccount.BankAccount(Bank._account_number)
        Bank._accounts.append(new_account)
        print('Account created successfully, your account number is: {}. \n'.format(new_account.account_number))

    def get_account(self, account_number):
        for account in Bank._accounts:
            if account.account_number == account_number:
                return account
        print('The account number you provided is not in our records. \n')
        return None

    def deposit(self):
        account_number = int(input('Please enter the account number you would like the deposit into: '))
        deposit_amount = float(input('Please enter the amount you would like the deposit: '))
        account = Bank.get_account(self, account_number)
        if account is not None:
            account.deposit(deposit_amount)
        else:
            print('The account number you gave does not match any in our records')

    def withdraw(self):
        account_number = int(input('Please enter the account number you would like the withdrawal from: '))
        withdraw_amount = float(input('Please enter the amount you would like the withdrawal: '))
        account = Bank.get_account(self, account_number)
        if account is not None:
            account.withdrawal(withdraw_amount)
        else:
            print('The account number you gave does not match any in our records')

    def check_balance(self):
        account_number = int(input('Please enter the account number you would like the check: '))
        account = Bank.get_account(self, account_number)
        if account is not None:
            account.display_account_details()


    def transfer(self):
        account_number_one = int(input('Please enter the account you would like to transfer OUT of: '))
        account_number_two = int(input('Please enter the account you would like to transfer INTO: '))
        transfer_amount = float(input('Please enter the amount you would like to transfer between the two accounts: '))
        account_one = Bank.get_account(self, account_number_one)
        account_two = Bank.get_account(self, account_number_two)
        if account_one is not None and account_two is not None:
            if account_one.withdrawal(transfer_amount):
                account_two.deposit(transfer_amount)
        else:
            print('One of the account numbers you gave does not match any in our records')
