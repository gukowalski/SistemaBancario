from ContaBancaria import ContaBancaria

class Cliente:
    
    def __init__(self, name: str, cpf: str, num: str):
        self._name = name
        self._cpf = cpf
        self._num = num
        self._accounts = []

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'O Cliente {self._name} está ativado, e possue {len(self._accounts)} conta'

    def create_account(self):
        account = ContaBancaria(self)
        self._accounts.append(account)
        return 'Conta criada com sucesso'
    
    def view_accounts(self):
        for conta in self._accounts:
            print(conta)

    def open_account(self, acc_number):
        for account in self._accounts:
            if not account.__account_number == acc_number:
                return 'A conta não existe' 
            return account
        
        