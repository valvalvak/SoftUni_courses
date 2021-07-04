class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balace = balance

    def credit(self, amount):
        self.balace += amount
        return self.balace

    def debit(self, amount):
        if amount <= self.balace:
            self.balace -= amount
            return self.balace
        return "Amount exceeded balance"

    def info(self):
        pass


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
