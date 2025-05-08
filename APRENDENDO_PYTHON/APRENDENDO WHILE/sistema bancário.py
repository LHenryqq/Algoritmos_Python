#sistema bancário
clientes = []
while True: 
    print("Realize seu cadastro.")
    nome = str(input("Digite seu nome completo: "))
    cpf = int(input("Digite seu CPF: "))
    rg = int(input("Digite seu RG: "))
    telefone = int(input("Digite seu telefone: ")) 
    agencia = input("Digite o número da sua agência: ")
    conta = input("Digite o número da conta: ")
    saldo = float(input("Saldo inicial: R$"))
    cliente = [nome, cpf, rg, telefone, agencia, conta, saldo]
    clientes.append(cliente)
    print("\nCadastro Realizado com sucesso. \nNome:", cliente[0],"\nCPF:", cliente[1],"\nRG:",cliente[2],"\nTelefone:",cliente[3],"\nAgência:",cliente[4],"\nConta: ",cliente[5],"\nSaldo: R$",cliente[6])

    while True:
        print("======SELECIONE A FUNÇÃO QUE DESEJA REALIZAR======")
        print("1- Ver saldo")
        print("2- Depositar")
        print("3- Sacar")
        print("4- Sair")
        funcao = input("Selecione a opção que deseja: ")
        saldo = saldo

        if funcao == "1":
            print("Seu saldo atual é: ", saldo)
        elif funcao == "2":
            deposito = float(input("Valor do depósito: "))
            if deposito < 0:
                print("Valor inválido.")
            saldo = saldo+deposito
            print("Depósito realizado com sucesso!. Foi adicionado R$",deposito,"à sua conta.")
        elif funcao == "3":
            saque = float(input("Valor do saque: "))
            if saque > saldo:
                print("Saldo insuficiente.")
            elif saldo >= saque:
                saldo = saldo-saque
                print("Saque realizado com sucesso!. Foi retirado R$",saque,"da sua conta.")
        elif funcao == "4":
            break
        else:
            print("Escolha uma opção válida.")