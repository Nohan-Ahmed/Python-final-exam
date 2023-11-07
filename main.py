from bank import Account


def register():
    # user input section
    name = input('Account name: ')
    email = input('Emial: ')
    address = input('Address: ')
    account_type = input(
        'Account types Savings or Current & admin (sv/cr/ad): ').lower()
    # create account based on input.
    match (account_type):
        case 'sv':
            return Account(name, email, address, 'savings')
        case 'cr':
            return Account(name, email, address, 'current')
        case 'ad':
            return Account(name, email, address, 'admin')
        case _:
            print("\n##### Invalid option #####")
            return None


def main():
    alice = Account('Alice', 'alice@gmail.com', 'MooN', 'sv')
    olivia = Account('Olivai Radrigo', 'olivia@gmail.com', 'MooN', 'cr')
    selena = Account('Selena Gomez', 'selena@gmail.com', 'MooN', 'sv')
    current_user = None

    while (True):
        if current_user == None:
            print(f'\n--------------------------------------')
            print("\tNo user is loged in!")
            print(f'--------------------------------------')
            op = input('Register or Login (R/L): ').lower()
            if op == 'r':
                current_user = register()
                if current_user != None:
                    print(
                        f'\n-------------------------------------------------------------------\n'
                    )
                    print(
                        f'Your Account is created successfully account type "{current_user.accountType}"  and account Num: {current_user.accNo}'
                    )

            elif (op == 'l'):
                try:
                    email = input("Enter your email: ")
                    accNo = int(input("Enter your Account No: "))
                except ValueError as e:
                    print(f"Error: {e}")
                for account in Account.accounts:
                    if account.accNo == accNo and account.email == email:
                        current_user = account
                        break
                else:
                    print(
                        "\n**Email and account number don't match. Please try again!"
                    )
            else:
                print(
                    f'\n---------------- Status --------------\n'
                )
                print("** Invalid option. Please try again.")

        else:
            print(
                f'\n-------------------- Wellcome back {current_user.name} ---------------------\n'
            )
            if current_user.accountType == 'admin':
                print('1. create an account')
                print('2. delete any user account')
                print('3. see all user accounts')
                print('4. check the total available balance of the bank.')
                print('5. check the total loan.')
                print('6. on & off the loan feature of the bank.')
                print("7. Logout")

                try:
                    op = int(input('\nChoise the opetion: '))
                    match (op):
                        case 1:
                            new_account = register()
                            print(
                                f'\n----------------------------------------------------------------\n'
                            )
                            print(
                                f'Your Account is created successfully account type "{new_account.accountType}"  and account Num: {new_account.accNo}'
                            )
                        case 2:
                            account_no = int(input("Account No: "))
                            current_user.delete_account(account_no)
                        case 3:
                            print(
                                "\n-------------------- Showing all users ---------------------\n"
                            )
                            for user in Account.accounts:
                                print(
                                    f'User name: {user.name}, email: {user.email}, account no: {user.accNo}'
                                )
                        case 4:

                            print(
                                f'\nTotal available balance of the bank: {current_user._total_balance}\n'
                            )
                        case 5:
                            print(
                                f'\nTotal loan amount: {current_user._total_loan}\n'
                            )
                        case 6:
                            op = input(
                                'Press "Y" to enable bank loan feature and disable "N" (Y/N): '
                            ).lower()
                            print(
                                f'\n----------------------------------------------------------------\n'
                            )
                            if op == 'y':
                                Account.isLoan = True
                                print(
                                    f"Bank Loan feature has been successfully enabled."
                                )
                            elif (op == 'n'):
                                print(
                                    f"Bank Loan feature has been successfully disabled."
                                )
                                Account.isLoan = False
                            else:
                                print("\n##### Invalid option #####")
                        case 7:
                            current_user = None
                        case _:
                            print("\n##### Invalid option #####")
                except Exception as e:
                    print(f'Error: {e}')
            else:
                print("1. Deposit")
                print("2. withdraw")
                print("3. transfer money")
                print("4. take a loan")
                print("5. check balance")
                print('6. Transaction history')
                print("7. Logout")
                try:
                    op = int(input("Chose the opetion: "))
                    match (op):
                        case 1:
                            amount = int(input("Deposit amount: "))
                            print(
                                "\n--------------------------------------------------------\n"
                            )
                            current_user.deposit(amount)
                        case 2:
                            amount = int(input("Withdraw amount: "))
                            print(
                                "\n--------------------------------------------------------\n"
                            )
                            current_user.withdraw(amount)
                        case 3:
                            amount = int(input("transfer amount: "))
                            accNo = int(input("transfer account no: "))
                            print(
                                "\n-------------------------------------------------------\n"
                            )
                            current_user.transfer_money(accNo, amount)
                        case 4:
                            amount = int(input("Loan amount: "))
                            print(
                                "\n------------------ Loan status ------------------------\n"
                            )
                            current_user.take_loan(amount)
                        case 5:
                            print(
                                f"----> Your current balance is: ${current_user.balance}"
                            )
                        case 6:
                            print(
                                "\n-------------- Show all transaction history ------------------\n"
                            )
                            current_user.show_transaction_history()
                        case 7:
                            current_user = None
                        case _:
                            print("\n##### Invalid option #####")
                except Exception as e:
                    print(f'Some error is occured: {e}')


if __name__ == '__main__':
    main()
