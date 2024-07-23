from collections import deque
from typing import List


class Transaction:
    def __init__(self, name, time, amount, city, index):
        self.name = name
        self.time = time
        self.amount = amount
        self.city = city
        self.index = index

    def __repr__(self):
        return f"{self.name},{self.time},{self.amount},{self.city}"

    def __str__(self):
        return f"{self.name},{self.time},{self.amount},{self.city}"


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)

        transaction_objects = []

        for i in range(n):
            transaction = transactions[i]
            name, time, amount, city = transaction.split(",")
            # Each transaction will be represented by a tuple (name, time, amount, city, i)
            transaction_objects.append(Transaction(name, int(time), int(amount), city, i))
        # Sort the transactions in increasing order by time
        transaction_objects.sort(key=lambda x: x.time)
        # Store the transactions of the last 60 minutes
        recent_transactions = {}
        invalid_transactions_indices = set()

        for transaction in transaction_objects:
            if transaction.name not in recent_transactions:
                recent_transactions[transaction.name] = deque()

            recent_transactions[transaction.name].append(transaction)
            recent_cities = set()

            i = 0
            # Popping transactions that happened before the last 60 minutes
            while i < len(recent_transactions[transaction.name]):
                earliest_transaction = recent_transactions[transaction.name][i]

                if earliest_transaction.time < transaction.time - 60:
                    recent_transactions[transaction.name].popleft()
                    continue

                recent_cities.add(earliest_transaction.city)
                i += 1
            # Setting the transactions that occurred in the last 60 minutes as invalid if they occurred in more than one city
            if len(recent_cities) > 1:
                for recent_transaction in recent_transactions[transaction.name]:
                    invalid_transactions_indices.add(recent_transaction.index)
            # A transaction is invalid if the amount exceeds $1000
            if transaction.amount > 1000:
                invalid_transactions_indices.add(transaction.index)
        # Building the output from the invalid transaction indices
        invalid_transactions = []

        for i in range(n):
            if i in invalid_transactions_indices:
                invalid_transactions.append(transactions[i])

        return invalid_transactions

