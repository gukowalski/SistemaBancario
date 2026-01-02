from datetime import datetime, timedelta

class Cliente:
    
    def __init__(self, name, cpf, num):
        self._name = name
        self._cpf = cpf
        self._num = num
        self._accounts = []

    def __str__(self):
        return f'O Cliente {self._name} está ativado, e possue {len(self._accounts)} contas'


 