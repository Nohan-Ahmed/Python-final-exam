class Account:
    accounts = []  # track all accounts.
    _total_balance = 10000
    _total_loan = 0
    isLoan = True

    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.accNo = len(Account.accounts) + 100
        self.email = email
        self.address = address
        self.accountType = account_type

        self.__balance = 0
        self._track_loans = 0
        self.__isBankrupt = False

        # track history.

        # list of dictinary with transaction amount and where.
        self._transaction_history = list()
        # add each instance to the accounts list
        Account.accounts.append(self)

    # method for balance.

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, val):
        self.__balance = val

    #is Bankrupt
    @property
    def isBankrupt(self) -> bool:
        return self.__isBankrupt

    @isBankrupt.setter
    def isBankrupt(self, val):
        self.__isBankrupt = val

    # withdraw & deposit system
    def deposit(self, amount):
        if not self.isBankrupt:
            if amount > 0:
                self.balance += amount
                Account._total_balance += amount
                print(f"You have successfully deposited: ${amount}")

    def withdraw(self, amount):
        if self.isBankrupt == False and self.balance > amount:
            self.balance -= amount
            Account._total_balance -= amount
            print(f"You have successfully withdraw: ${amount} ")
            return amount
        else:
            print("Withdrawal amount exceeded")

    def transfer_money(self, receiver_accNo, amount):
        if self.balance > amount:
            if self.isBankrupt == False:
                for account in Account.accounts:
                    if account.accNo == receiver_accNo:
                        if account.accountType == 'admin':
                            print(
                                "You can't transfer money to the admin account!"
                            )
                            return
                        elif self.accNo == receiver_accNo:
                            print(
                                "You can't transfer money to your own account."
                            )
                            return

                        self.balance -= amount
                        account.balance += amount
                        self._transaction_history.append({account: amount})
                        print(
                            f"${amount} successfully transferred from account number: {account.accNo}\n"
                        )
                        print(
                            f'---> Your current balance is now: ${self.balance}'
                        )
                        return
                else:
                    print(f'Account Nnumber: {receiver_accNo} does not exist')
                    return
            else:
                print('the bank is bankrupt.'.capitalize())
                return
        else:
            print(
                f"You don't have enough money, your current balance: {self.balance}"
            )

    def show_transaction_history(self):
        for item in self._transaction_history:
            for k, v in item.items():
                print(f'Account no: {k.accNo}, transaction: ${v}')
        if len(self._transaction_history) == 0:
            print("No transactions yet!")

    def take_loan(self, amount):
        if amount > 0:
            if self._track_loans != 2 and Account.isLoan:
                self.balance += amount
                self._track_loans += 1
                Account._total_balance -= amount
                Account._total_loan += amount
                print(
                    f"You got a ${amount} loan, your current balance is ${self.balance}"
                )
            else:
                print(f"You are unable to take loan!")
        else:
            print("Loan amount is very low, please try again!")

    # delete an account
    def delete_account(self, accountNo):
        if self.accountType == 'admin':
            for ind, account in enumerate(Account.accounts):
                if account.accNo == accountNo:
                    obj = Account.accounts.pop(ind)
                    print(
                        f'Account number {obj.accNo} has been deleted successfully'
                    )
                    return obj

            else:
                print(f"\n##### Invalid account number: {self.accNo} #####")

        else:
            print("Admin only remove!")


def register():
    # user input section
    name = input('Account name: ')
    email = input('Emial: ')
    address = input('Address: ')
    account_type = input(
        'Account types Savings or Current & admin (SV/CR): ').lower()

    # create account based on input.
    match (account_type):
        case 'sv':
            return Account(name, email, address, 'savings')
        case 'cr':
            return Account(name, email, address, 'current')
        case _:
            print(f'\n----------------------------------------')
            print("\n##### Invalid account type #####")
            return None


def main():
    admin = Account("admin", 'admin123@gmail.com', 'Japan', 'admin')
    current_user = None

    # infiti loop start.
    while (True):
        # if current_user=
        print(f'--------------- Status ----------------')
        print("1. Admin\n2. Users\n3. Exit")
        try:
            choice = int(input("Enter you choice: "))
        except Exception as e:
            print("\n--------------------------------------------------------")
            print(f"Error raised: {e}")
            print("--------------------------------------------------------")
            continue

        if (choice == 1):
            # this code part for admin.
            print("\n--------------------------------------------------------")
            print(
                f'Admin Name = {admin.name} | Admin password = {admin.accNo}')
            print("--------------------------------------------------------\n")

            name = input("Enter the admin name: ")
            passwd = input("Enter the admin password: ")
            if admin.name == name and str(admin.accNo) == passwd:
                current_user = admin
                print(
                    f'\n-------------------- Wellcome back {current_user.name} ---------------------\n'
                )

                while (True):
                    print('1. create an account')
                    print('2. delete any user account')
                    print('3. see all user accounts')
                    print('4. check the total available balance of the bank.')
                    print('5. check the total loan.')
                    print('6. Enable Loan feature')
                    print('7. Disable Loan feature')
                    print("8. Logout")

                    try:
                        op = int(input('\nChoise the opetion: '))
                        match (op):
                            case 1:
                                new_account = register()
                                print(
                                    f'\n----------------------------------------------------------------'
                                )
                                print(
                                    f'\nYour Account is created successfully account type "{new_account.accountType}"  and account Num: {new_account.accNo}\n'
                                )
                            case 2:
                                account_no = int(input("Account No: "))
                                print(
                                    f'\n----------------------------------------------------------------'
                                )
                                current_user.delete_account(account_no)

                            case 3:
                                print(
                                    "\n-------------------- Showing all users ---------------------\n"
                                )
                                for user in Account.accounts:
                                    if user == admin:
                                        continue
                                    print(
                                        f'User name: {user.name}, email: {user.email}, account no: {user.accNo}'
                                    )
                            case 4:
                                print(
                                    f'\n----------------------------------------------------------------'
                                )
                                print(
                                    f'Total available balance of the bank: ${current_user._total_balance}'
                                )
                            case 5:
                                print(
                                    f'\n----------------------------------------------------------------'
                                )
                                print(
                                    f'Total loan amount: ${current_user._total_loan}'
                                )
                            case 6:

                                print(
                                    f'\n----------------------------------------------------------------'
                                )
                                Account.isLoan = True
                                print(
                                    f"Bank Loan feature has been successfully enabled."
                                )

                            case 7:
                                print(
                                    f'\n----------------------------------------------------------------'
                                )
                                Account.isLoan = False
                                print(
                                    f"Bank Loan feature has been successfully disabled."
                                )

                            case 8:
                                print(
                                    f'\n----------------------------------------------------------------'
                                )
                                current_user = None
                                print("You successfully logout!")
                                break
                            case _:
                                print(
                                    "\n--------------------------------------------------------"
                                )
                                print("##### Invalid option #####")
                    except Exception as e:
                        print(f'Error: {e}')

                    print(
                        f'----------------------------------------------------------------\n'
                    )
            else:
                print(f'\n--------------------------------------\n')
                print("Invalid username or password!")

        elif choice == 2:
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
                        # end notation.
                        print(
                            f'\n-------------------------------------------------------------------\n'
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
                                f'\n-------------------------------------------------------------------\n'
                            )
                            print(
                                "\n**Email and account number don't match. Please try again!"
                            )
                    else:
                        print(f'\n---------------- Status --------------\n')
                        print("** Invalid option. Please try again.")

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
                                    f'\n--------------------------------------------------------\n'
                                )
                                print(
                                    f"----> Your current balance is: ${current_user.balance}"
                                )
                            case 6:
                                print(
                                    "\n-------------- Show all transaction history ------------------\n"
                                )
                                current_user.show_transaction_history()
                            case 7:
                                print(
                                    f'\n--------------------------------------------------------'
                                )
                                print("You successfully logout!")
                                current_user = None
                                print(
                                    f'--------------------------------------------------------\n'
                                )
                                break
                            case _:
                                print(
                                    f'\n--------------------------------------------------------\n'
                                )
                                print("\n##### Invalid option #####")
                    except Exception as e:
                        print(f'Some error is occured: {e}\n')

                    print(
                        f'\n--------------------------------------------------------\n'
                    )
        elif choice == 3:
            print("\n--------------------------------------------------------")
            print("\tProgram terminated successfully!".expandtabs(12))
            print("--------------------------------------------------------\n")
            break


if __name__ == "__main__":
    main()
