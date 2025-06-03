cadastro = []
 
while True:
    print("\n############## MENU ##############")
    print("1 = Cadastrar")
    print("2 = Consultar Cadastro")
    print("3 = Sair")
    print("###################################")
 
    try:
        opcao = int(input("Escolha uma opção: "))
 
        if opcao == 1:
            while True:
                print("\n########## CADASTRAR USUÁRIO ##########")
                try:
                    nome = input("Digite o nome: ").strip().title()
                    idade = int(input("Digite a idade: "))
                    cpf = input("Digite o CPF: ").strip()
                    sexo = input("Digite o sexo (M/F): ").strip().upper()
                    endereco = input("Digite o endereço: ").strip()
                    cidade = input("Digite a cidade: ").strip()
                    estado = input("Digite o estado: ").strip().upper()
 
                    dados = {
                        "Nome": nome,
                        "Idade": idade,
                        "CPF": cpf,
                        "Sexo": sexo,
                        "Endereço": endereco,
                        "Cidade": cidade,
                        "Estado": estado
                    }
 
                    cadastro.append(dados)
 
                    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
                        arquivo.write(f"Nome: {nome}, Idade: {idade}, CPF: {cpf}, Sexo: {sexo}, Endereço: {endereco}, Cidade: {cidade}, Estado: {estado}\n")
 
                    continuar = input("Deseja cadastrar outro usuário? (S/N): ").strip().upper()
                    if continuar != 'S':
                        break
 
                except ValueError:
                    print("Erro: Valor inválido. Tente novamente.")
 
        elif opcao == 2:
            print("\n########## CONSULTA DE CADASTROS ##########")
            try:
                with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    if conteudo:
                        print(conteudo)
                    else:
                        print("Nenhum cadastro encontrado.")
            except FileNotFoundError:
                print("Arquivo de cadastro não encontrado.")
 
        elif opcao == 3:
            print("Saindo do programa. Dados salvos com sucesso!")
            break
 
        else:
            print("Opção inválida. Tente novamente.")
 
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")