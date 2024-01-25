import Bank

bank = Bank.Bank('Brady\'s Savings Bank')


def menu():
    print("Welcome to {}, Please select an option listed below: \n "
          "1) Create an account \n "
          "2) Deposit \n "
          "3) Withdraw \n "
          "4) Check Balance \n "
          "5) Transfer \n "
          "9) Quit \n".format(bank.name))


def execute_choice():
    try:
        menu()
        user_input = int(input("Please enter a selection from the menu above: "))
        if user_input == 1:
            bank.create_account()
        elif user_input == 2:
            bank.deposit()
        elif user_input == 3:
            bank.withdraw()
        elif user_input == 4:
            bank.check_balance()
        elif user_input == 5:
            bank.transfer()
        elif user_input == 9:
            exit() # There are two ways to end the program, through this method or by entering no into the recursive call.
        else:
            print("Please enter the number of an option.")
    except ValueError:
        print("Please enter a number.")


# This implementation is not preferred, but its most straight forward way I could think to make a
# "continue_operation" function which calls itself in a recursive manner.
def continue_operation():
    value = input("Would you like to continue performing operations? Enter yes to continue and no to exit: ")
    if value.lower() == 'yes':
        execute_choice()
    elif value.lower() == 'no':
        exit() # the other ways to exit is from the menu selection. This is only here to make the call recursive.
    continue_operation()


continue_operation()

