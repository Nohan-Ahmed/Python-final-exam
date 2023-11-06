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
        self._loan = 0
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
                print(
                    f"${amount} has been successfully deposited to account number: {self.accNo}"
                )

    def withdraw(self, amount):
        if self.isBankrupt == False and self.balance > amount:
            self.balance -= amount
            Account._total_balance -= amount
            print(
                f"${amount} successfully withdrawn to account number: {self.accNo}"
            )
            return amount
        else:
            print("Withdrawal amount exceeded")

    def transfer_money(self, receiver: object, amount):
        if self.balance > amount:

            if self.isBankrupt == False:
                for account in Account.accounts:
                    if account.accNo == receiver.accNo:
                        self.withdraw(amount)
                        receiver.deposit(amount)
                        self._transaction_history.append({receiver: amount})
                        # print("Elu milu kilu")
                        break
                else:
                    print('Account does not exist')
            else:
                print('the bank is bankrupt.'.capitalize())

    def show_transaction_history(self):
        for item in self._transaction_history:
            for k, v in item.items():
                print(f'Account no: {k.accNo}, transaction: ${v}')

    def take_loan(self, amount):
        if amount > 0 and self._loan != 2 and Account.isLoan:
            self.balance += amount
            self.loan -= 1
            Account._total_balance -= amount
            Account._total_loan += amount

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
