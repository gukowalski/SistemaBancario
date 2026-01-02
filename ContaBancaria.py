import random
from Cliente import Cliente
from datetime import datetime

class ContaBancaria:
    
    def __init__(self, owner: Cliente):
        self._account_number = random.randint(1, 100)
        self._balance = 0
        self._owner = owner
        self._creation_date = datetime.date

    def __str__(self):
        return f'A conta do proprietário {self._owner._name} tem o saldo de R${self._balance}'