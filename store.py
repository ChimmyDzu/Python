import datetime

class Client:
    number_of_clients = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.transactions = []
        Client.number_of_clients += 1

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


class Item:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


class Transaction:
    def __init__(self, transaction_id, client, items):
        self.transaction_id = transaction_id
        self.client = client
        self.items = items
        self.time_stamp = datetime.datetime.now()

    def get_total_amount(self):
        return sum(item.price for item in self.items)


# Create clients
clients = []
clients.append(Client(1, "Džūlija"))
clients.append(Client(2, "Raimonds"))
clients.append(Client(3, "Kristians"))

# Create items
items = [
    Item(1, "Makeup", 100.99),
    Item(2, "Art supplies", 50.49),
    Item(3, "Basketball", 10.99),
    Item(4, "Video Game", 79.99)
]

# Create transactions and add them to clients
transactions = [
    Transaction(1, clients[0], [items[0], items[3]]),
    Transaction(2, clients[1], [items[3]]),
    Transaction(3, clients[2], [items[2], items[1], items[3]]),
    Transaction(4, clients[0], [items[2]])
]

# Adding transactions to  clients
clients[0].add_transaction(transactions[0])
clients[0].add_transaction(transactions[3])
clients[1].add_transaction(transactions[1])
clients[2].add_transaction(transactions[2])

# Main code
print('Welcome to my online shop "Hello Sunshine"')
print(f'Our shop had {Client.number_of_clients} clients today:')
print()

#nested loops

for client in clients:
    print(f'Client {client.name} has the following transactions:')
    for transaction in client.transactions:
        print(f'  Transaction[{transaction.transaction_id}] - Total: ${transaction.get_total_amount()}')
        print(f'    Timestamp: {transaction.time_stamp}')
        for item in transaction.items:
            print(f'    Item[{item.item_id}] {item.name}: ${item.price}')
