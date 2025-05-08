while True:
    print("Digite 'E' para registrar entrada")
    print("Digite 'S' para registrar saída")
    print("Digite 'R' para emitir um relatório")
    print("Digite 'X' para fechar o programa")
    acao = input("Qual ação deseja realizar?: ").upper()
    estoque_inicial = ["10", "20", "30", "40", "50"]
    "10" == "Caderno"
    "20" == "Caneta"
    "30" == "Lápis"
    "40" == "Borracha"
    "50" == "Régua"
    caderno = 200
    caneta = 250
    lapis = 300
    borracha = 350
    regua = 150
    while True:
        if acao == "E":
            codigo = input("Insira o código do produto de entrada: ")
            if codigo == "10":
                quantidade = int(input("Quantidade de entrada: "))
                caderno = caderno + quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", caderno)
                break
            elif codigo == "20":
                quantidade = int(input("Quantidade de entrada: "))
                caneta = caneta + quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", caneta)
                break
            elif codigo == "30":
                quantidade = int(input("Quantidade de entrada: "))
                lapis = lapis + quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", lapis)
                break
            elif codigo == "40":
                quantidade = int(input("Quantidade de entrada: "))
                borracha = borracha + quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", borracha)
                break
            elif codigo == "50":
                quantidade = int(input("Quantidade de entrada: "))
                regua = regua + quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", regua)
                break
        elif acao == "S":
            codigo = input("Insira o código do produto de saída: ")
            if codigo == "10":
                quantidade = int(input("Quantidade de saída: "))
                if quantidade>caderno:
                    faltam = quantidade - caderno
                    print("Estoque insuficiente. Faltam",faltam,"itens para a entrega solicitada")
                    break
                caderno = caderno - quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", caderno)
                break
            elif codigo == "20":
                quantidade = int(input("Quantidade de saída: "))
                if quantidade>caneta:
                    faltam = quantidade - caneta
                    print("Estoque insuficiente. Faltam",faltam,"itens para a entrega solicitada")
                    break
                caneta = caneta - quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", caneta)
                break
            elif codigo == "30":
                quantidade = int(input("Quantidade de saída: "))
                if quantidade>lapis:
                    faltam = quantidade - lapis
                    print("Estoque insuficiente. Faltam",faltam,"itens para a entrega solicitada")
                    break
                lapis = lapis - quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", lapis)
                break
            elif codigo == "40":
                quantidade = int(input("Quantidade de saída: "))
                if quantidade>borracha:
                    faltam = quantidade - borracha
                    print("Estoque insuficiente. Faltam",faltam,"itens para a entrega solicitada")
                    break
                borracha = borracha - quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", borracha)
                break
            elif codigo == "50":
                quantidade = int(input("Quantidade de saída: "))
                if quantidade>regua:
                    faltam = quantidade - regua
                    print("Estoque insuficiente. Faltam",faltam,"itens para a entrega solicitada")
                    break
                regua = regua - quantidade
                print("Atualizada quantidade em estoque, estoque atual é:", regua)
                break
        elif acao == "R":
            print("RELATÓRIO: \n Caderno:",caderno,"\nCaneta:",caneta,"\nLapis:",lapis,"\nBorracha:",borracha,"\nRégua:",regua)
        elif acao != "E" and acao != "S" and acao != "R" and acao != "X":
            print("Selecione uma opção válida.")
        elif acao == "X":
            print("Sistema encerrado.")
            break
        break