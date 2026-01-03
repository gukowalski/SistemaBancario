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
            if account._account_number == acc_number:
                return account
      
    def deposit(self, acc_number, amount):
        account = self.open_account(acc_number)

        if account is None:
            return "Conta não existe"

        account.deposit(amount)
        return "O deposito na conta foi efetuado com sucesso"
    
    def withdrawal(self, acc_number, amount):
        account = self.open_account(acc_number)

        if account is None:
            return "Conta não existe"
        
        account.withdrawal(amount)
        return "Saque realizado com sucesso"