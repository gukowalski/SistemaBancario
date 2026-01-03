import random
from datetime import datetime

class ContaBancaria:
    
    def __init__(self, owner):
        self._account_number = random.randint(1, 100)
        self._balance = 0
        self._owner = owner
        self._creation_date = datetime.now().date()

    def __str__(self):
        return f'A conta numero {self._account_number} tem o saldo de R${self._balance}'