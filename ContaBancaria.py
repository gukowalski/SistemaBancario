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
    
    def deposit(self, amount):
        self._balance = self._balance + amount
        return f'Deposito realizado com sucesso no valor de R${amount}'
    
    def withdrawal(self, amount):
        if self._balance < amount:
            return f'O saldo é menor que o valor desejado para saque'
        self._balance = self._balance - amount
        return f'Saque realizado com sucesso no valor de R${amount}, valor da conta agora é R${self._balance}'
    
    @property
    def check_balance(self):
        return self._balance