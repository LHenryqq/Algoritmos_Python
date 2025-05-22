#MENU
while True:
    print("Pressione '1' para Cadastros \nPressione '2' para Relatórios \nPressione '3' para Fechar o programa.")
    try:
        acao = int(input("Qual ação deseja realizar: "))
    except ValueError:
        print("Digite apenas números.")
    while True:
        if acao == 1:
            print(("CADASTROS:"))
            print("Pressione '1' para Cadastro de Clientes \nPressione '2' para Cadastro de Passagens \n Pressione '3' para Cadastro de Aviões \nPressione '4' para Cadastro de Tripulação")
            cadastro = int(input("Qual Cadastro deseja realizar: "))
            if cadastro == 1:
                #CADASTRO DE CLIENTE
                print("Cadastro do cliente:")
                nome = input("Nome: ")
                sobr = input("Sobrenome: ")
                try:
                    rg = int(input("RG: "))
                    cpf = int(input("CPF: "))
                    fone = int(input("Fone: "))
                    idade = int(input("Idade: "))
                except ValueError:
                    print("Digite apenas números.")
                endereco = input("Endereço: ")
                break
            elif cadastro == 2:
                print("Cadastro de Passagem:")
                destino = input("Destino: ")
                origem = input("Origem: ")
                try:
                    duração = float(input("Duração em minutos: "))
                    valor_passagem = float(input("Valor da Passagem: "))
                except ValueError:
                    print("Digite apenas números.")
                desconto = valor_passagem*(5/100)
                break
            elif cadastro == 3:
                print("Cadastro do Avião: ")
                modelo = input("Modelo da aeronave: ")
                try:
                    ano = int(input("Ano da aeronave: "))
                    horas_voo = int(input("Horas de voo da aeronave: "))
                except ValueError:
                    print("Digite apenas números.")
                cor = input("Cor da aeronave: ")
                passageiros = int(input("Quantidade de passageiros na aeronave: "))
                break
            elif cadastro == 4:
                print("Cadastro da Tripulação: ")
                nome = input("Nome: ")
                cargo = input("Cargo: ")
                try:
                    idade = int(input("Idade: "))
                    fone = int(input("Fone: "))
                except ValueError:
                    print("Digite apenas números")
                data_admissao = input("Data de Admissão: ")
                break
            else:
                print("Digite uma opção válida.")
                break
    while True:
        if acao == 2:
            #RELATÓRIOS
            print("RELATÓRIOS: ")
            print("Pressione '1' para Relatório dos Clientes \nPressione '2' para Relatório das Passagens \n Pressione '3' para Relatório do Avião \nPressione '4' para Relatório da Tripulação")
            relatorio = int(input("Qual relatório deseja: "))
            if relatorio == 1:
                print("Relatório de Passageiros")
