from Cliente import Cliente
print("Iniciando sistema de banco...")

print("Vamos criar seu usuário Cliente ok ?")
print("")

name = input("Seu nome completo ? ")
cpf = input("Qual seu cpf ? ")
num = input("E seu número de telefone ? ")

cliente = Cliente(name, cpf, num)

print("Sua cliente está criada com sucesso")

print(f" Vamos criar sua conta, tudo certo ? ")

cliente.create_account()


option = 0

while option != 4:
    print("\n--- MENU ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Mostrar suas contas")
    print("4 - Sair")

    option = int(input("Qual opção você deseja realizar? "))

    if option == 1:
        print(cliente.view_accounts())
        account = int(input("Qual o número da conta que deseja depositar? "))
        amount = float(input("Digite o valor que deseja depositar: "))
        cliente.deposit(account, amount)

    elif option == 2:
        print(cliente.view_accounts())
        account = int(input("Qual o número da conta que deseja sacar? "))
        amount = float(input("Digite o valor que deseja sacar: "))
        cliente.withdrawal(account, amount)

    elif option == 3:
        print(cliente.view_accounts())
    else:
        print("Opção inválida — tente novamente.")