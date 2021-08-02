from typing import List


class Account:
    default_starting_amount = 0

    def __init__(self, owner, amount=default_starting_amount):
        self.owner: str = owner
        self.amount: int = amount
        self._transactions: List = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            account.add_transaction(amount_to_add)
            return f"New balance: {account.balance}"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __lt__(self, other):
        return self.balance < other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        sums = self.amount + other.amount
        result = Account(f"{self.owner}&{other.owner}", sums)
        result._transactions = self._transactions + other._transactions
        return result

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"


#
# acc = Account('bob', 10)
# acc2 = Account('john')
# print(acc)
# print(repr(acc))
# acc.add_transaction(20)
# acc.add_transaction(-20)
# acc.add_transaction(30)
# print(acc.balance)
# print(len(acc))
# for transaction in acc:
#     print(transaction)
# print(acc[1])
# print(list(reversed(acc)))
# acc2.add_transaction(10)
# acc2.add_transaction(60)
# print(acc > acc2)
# print(acc >= acc2)
# print(acc < acc2)
# print(acc <= acc2)
# print(acc == acc2)
# print(acc != acc2)
# acc3 = acc + acc2
# print(acc3)
# print(acc3._transactions)
# import unittest
#
#
# class TestsAccount(unittest.TestCase):
#     def setUp(self):
#         self.acc1 = Account("Johhny")
#         self.acc2 = Account("Anna", 40)
#
#     def test_init(self):
#         self.assertEqual(self.acc1.owner, "Johhny")
#         self.assertEqual(self.acc1.amount, 0)
#         self.assertEqual(self.acc1._transactions, [])
#         self.assertEqual(self.acc2.owner, "Anna")
#         self.assertEqual(self.acc2.amount, 40)
#         self.assertEqual(self.acc2._transactions, [])
#
#     def test_repr(self):
#         self.assertEqual("Account(Johhny, 0)", repr(self.acc1))
#
#     def test_str(self):
#         self.assertEqual("Account of Anna with starting amount: 40", str(self.acc2))
#
#     def test_add_transaction(self):
#         self.acc1.add_transaction(10)
#         self.assertEqual(self.acc1._transactions, [10])
#         with self.assertRaises(ValueError) as cm:
#             self.acc1.add_transaction(9.9)
#         self.assertEqual(str(cm.exception), "please use int for amount")
#
#     def test_balance(self):
#         self.acc2.add_transaction(-20)
#         self.assertEqual(self.acc2.balance, 20)
#
#     def test_len(self):
#         self.acc1.add_transaction(10)
#         self.acc1.add_transaction(-5)
#         self.assertEqual(len(self.acc1), 2)
#
#     def test_get_item(self):
#         self.acc1.add_transaction(5)
#         self.assertEqual(self.acc1[0], 5)
#
#
# if __name__ == "__main__":
#     unittest.main()
