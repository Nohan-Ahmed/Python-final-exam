from multipledispatch import dispatch


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
                        if account.type == 'admin':
                            print("You can't send money to the admin account!")
                            return
                        self.balance -= amount
                        account.balance += amount
                        self._transaction_history.append({account: amount})
                        print(
                            f"${amount} successfully transferred from account number: {account.accNo}"
                        )
                        print(f'Your current balance is now: ${self.balance}')
                        return
                else:
                    print(f'Account No {receiver_accNo} does not exist')
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
        if amount > 0 and self._track_loans != 2:
            if Account.isLoan == False:
                print("Loan ")
            self.balance += amount
            self._track_loans -= 1
            Account._total_balance -= amount
            Account._total_loan += amount
            print(
                f"You got a ${amount} loan, your current balance is ${self.balance}"
            )

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
                print("\n##### Invalid account number! #####")

        else:
            print("Admin only remove!")
