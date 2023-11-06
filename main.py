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
    alice = Account('Alice', 'alice@gmail.com', 'MooN', 'admin')
    current_user = None

    while (True):
        if current_user == None:
            print(f'\n--------------------------------------')
            print("\tNo user is loged in!")
            print(f'--------------------------------------')
            op = input('Register or Login (R/L): ').lower()
            if op == 'r':
                current_user = register()

            elif (op == 'l'):
                email = input("Enter your email: ")
                accNo = int(input("Enter your Account No: "))
                for account in Account.accounts:
                    if account.accNo == accNo and account.email == email:
                        current_user = account
                        break
                else:
                    print(
                        "\n!!!!!!! Account no && password didn't match. please try agin !!!!!!!"
                    )
            else:
                print("\n##### Invalid option #####")
                break
        else:
            print(
                f'\n----------------Wellcome back {current_user.name} ------------------\n'
            )
            if current_user.accountType == 'admin':
                print('1. create an account')
                print('2. delete any user account')
                print('3. see all user accounts')
                print('4. check the total available balance of the bank.')
                print('5. check the total loan.')
                print('6. on or off the loan feature of the bank.')
                print("7. Logout")

                op = int(input('\nChoise the opetion: '))
                match (op):
                    case 1:
                        register()
                    case 2:
                        account_no = int(input("Account No: "))
                        current_user.delete_account(account_no)
                    case 3:
                        print(
                            "\n----------------- Showing all users ------------------\n"
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
                        op = input('on or off (Y/N): ').lower()
                        if op == 'y':
                            Account.isLoan = True
                        elif (op == 'n'):
                            Account.isLoan = False
                        else:
                            print("\n##### Invalid option #####")
                    case 7:
                        current_user = None
                    case _:
                        print("\n##### Invalid option #####")
            else:
                print("1. Deposit")
                print("2. withdraw")
                print("3. transfer money")
                print("4. take a loan")
                print("5. check balance")
                print("6. Logout")
                op = int(input("Chose the opetion: "))
                match (op):
                    case 1:
                        amount = int(input("Deposit amount: "))
                        current_user.deposit(amount)
                    case 2:
                        amount = int(input("Withdraw amount: "))
                        current_user.withdraw(amount)
                    case 3:
                        amount = int(input("transfer amount: "))
                        current_user.transfer_money(amount)
                    case 4:
                        amount = int(input("Loan amount: "))
                        current_user.take_loan(amount)
                    case 5:
                        print(
                            f"----> Your current balance is: ${current_user.balance}"
                        )
                    case 6:
                        current_user = None
                    case _:
                        print("\n##### Invalid option #####")


if __name__ == '__main__':
    main()
