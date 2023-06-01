class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Гроші успішно додані на рахунок. Поточний баланс:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Гроші успішно зняті з рахунку. Поточний баланс:", self.balance)
        else:
            print("Недостатньо коштів на рахунку.")

    def get_balance(self):
        print("Поточний баланс:", self.balance)
        account1 = BankAccount("123456789", 1000)
        account1.get_balance()
        account1.deposit(500)
        account1.withdraw(200)
        account1.get_balance()
