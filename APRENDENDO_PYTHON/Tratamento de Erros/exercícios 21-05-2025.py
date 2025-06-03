passageiros = {}
passagens_cadastradas = {}
avioes_cadastrados = {}
tripulacao_cadastrada = {}

while True: 
    print("\n#MENU PRINCIPAL#")
    print("Pressione '1' para Cadastros \nPressione '2' para Relatórios \nPressione '3' para Fechar o programa.")
    try:
        acao = int(input("Qual ação deseja realizar: "))
    except ValueError:
        print("Digite apenas números.")
        continue 

    while True: 
        if acao == 1:
            print(("\nCADASTROS:"))
            print("Pressione '1' para Cadastro de Clientes \nPressione '2' para Cadastro de Passagens \nPressione '3' para Cadastro de Aviões \nPressione '4' para Cadastro de Tripulação")
            try:
                cadastro = int(input("Qual Cadastro deseja realizar: "))
            except ValueError:
                print("Opção de cadastro inválida. Digite apenas números.")
                break 

            if cadastro == 1:
                print("\nCadastro do cliente:")
                nome = input("Nome: ")
                sobr = input("Sobrenome: ")
                rg, cpf, fone, idade = None, None, None, None
                try:
                    rg = int(input("RG: "))
                    cpf = int(input("CPF: "))
                    fone = int(input("Fone: "))
                    idade = int(input("Idade: "))
                except ValueError:
                    print("Erro: RG, CPF, Fone e Idade devem ser números. Cadastro parcialmente preenchido.")
                endereco = input("Endereço: ")
                passageiros["ultimo_cliente"] = {
                    "Nome": nome, 
                    "Sobrenome": sobr, 
                    "RG": rg, 
                    "CPF": cpf, 
                    "Fone": fone, 
                    "Idade": idade, 
                    "Endereco": endereco
                }
                print("Cliente processado.") 
                break 
            
            elif cadastro == 2:
                print("\nCadastro de Passagem:")
                destino = input("Destino: ")
                origem = input("Origem: ")
                duracao, valor_passagem = None, None
                try:
                    duracao = float(input("Duração em minutos: "))
                    valor_passagem = float(input("Valor da Passagem: R$"))
                    desconto = valor_passagem * (5 / 100) 
                    passagens_cadastradas["ultima_passagem"] = {
                        "Destino": destino,
                        "Origem": origem,
                        "Duração_min": duracao,
                        "Valor": valor_passagem,
                        "Desconto": desconto
                    }
                    print(f"Passagem processada. Desconto: R${desconto:.2f}")
                except ValueError:
                    print("Erro: Duração e Valor da Passagem devem ser números. Cadastro não realizado/preenchido.")
                break 

            elif cadastro == 3:
                print("\nCadastro do Avião: ")
                modelo = input("Modelo da aeronave: ")
                ano, horas_voo, quant_passageiros = None, None, None
                try:
                    ano = int(input("Ano da aeronave: "))
                    horas_voo = int(input("Horas de voo da aeronave: "))
                    quant_passageiros = int(input("Quantidade de passageiros na aeronave: "))
                except ValueError:
                    print("Erro: Ano, Horas de voo e Quantidade de passageiros devem ser números. Cadastro parcialmente preenchido.")
                cor = input("Cor da aeronave: ")
                avioes_cadastrados["ultimo_aviao"] = {
                    "Modelo": modelo,
                    "Ano": ano,
                    "Horas_voo": horas_voo,
                    "Cor": cor,
                    "Capacidade_Passageiros": quant_passageiros
                }
                print("Avião processado.")
                break 

            elif cadastro == 4:
                print("\nCadastro da Tripulação: ")
                nome = input("Nome: ")
                cargo = input("Cargo: ")
                idade, fone = None, None
                try:
                    idade = int(input("Idade: "))
                    fone = int(input("Fone: "))
                except ValueError:
                    print("Erro: Idade e Fone devem ser números. Cadastro parcialmente preenchido.")
                data_admissao = input("Data de Admissão (DD/MM/AAAA): ")
                tripulacao_cadastrada["ultimo_tripulante"] = {
                    "Nome": nome,
                    "Cargo": cargo,
                    "Idade": idade,
                    "Fone": fone,
                    "Data_Admissao": data_admissao
                }
                print("Tripulante processado.")
                break 
            else:
                print("Opção de cadastro inválida.")
                break 
        else: 
            break 

    while True:
        if acao == 2:
            print("\nRELATÓRIOS: ")
            print("Pressione '1' para Relatório dos Clientes \nPressione '2' para Relatório das Passagens \nPressione '3' para Relatório do Avião \nPressione '4' para Relatório da Tripulação")
            try:
                relatorio = int(input("Qual relatório deseja: "))
            except ValueError:
                print("Opção de relatório inválida. Digite apenas números.")
                break 

            if relatorio == 1:
                print("\nRelatório de Clientes:")
                if passageiros: 
                    print(passageiros)
                else:
                    print("Nenhum cliente cadastrado.")
            elif relatorio == 2:
                print("\nRelatório de Passagens:")
                if passagens_cadastradas:
                    print(passagens_cadastradas)
                else:
                    print("Nenhuma passagem cadastrada.")
            elif relatorio == 3:
                print("\nRelatório do Avião:")
                if avioes_cadastrados:
                    print(avioes_cadastrados)
                else:
                    print("Nenhum avião cadastrado.")
            elif relatorio == 4:
                print("\nRelatório da Tripulação:")
                if tripulacao_cadastrada:
                    print(tripulacao_cadastrada)
                else:
                    print("Nenhum tripulante cadastrado.")
            else:
                print("Opção de relatório inválida.")
            
            break 
        else: 
            break

    if acao == 3:
        print("Fechando o programa.")
        break 