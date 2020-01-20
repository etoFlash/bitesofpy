from functools import total_ordering


@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def _validate(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Amount should be int")

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __len__(self):
        return len(self._transactions)

    def __add__(self, amount):
        self._validate(amount)
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._validate(amount)
        self._transactions.append(-amount)

    def __getitem__(self, item):
        return self._transactions[item]

    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"
