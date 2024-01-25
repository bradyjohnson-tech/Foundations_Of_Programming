class BankAccount:
    _initial_balance = float(0.00)

    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = BankAccount._initial_balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            print('{} Dollars have been deposited in bank account {}'.format(deposit_amount, self.account_number))
            return True
        else:
            print('You may only deposit sums greater than 0.')
            return False

    def withdrawal(self, withdrawal_amount):
        if withdrawal_amount < 0:
            print('You may only withdrawal sums of money greater than 0.')
            return False
        elif withdrawal_amount > self.balance:
            print('Insufficient funds. The remaining balance is only {}'.format(self.balance))
            return False
        else:
            self.balance -= withdrawal_amount
            print('{} dollars have been withdrawn from your account. The remaining balance is {}'.format(withdrawal_amount, self.balance))
            return True

    def check_balance(self): # This method is described in the directions. I do not use but it is here becuase it was explicitely asked for.
        return self.balance

    def display_account_details(self):
        print(' Account Number: {} \n Account Balance: {}'.format(self.account_number, self.balance))



