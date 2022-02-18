class Account:
    def __init__(self):
        self.money = 0

    def deposit(self, amount):
        self.money += amount


account = Account()
money = 100
account.deposit(50)

print(money, account.money)
