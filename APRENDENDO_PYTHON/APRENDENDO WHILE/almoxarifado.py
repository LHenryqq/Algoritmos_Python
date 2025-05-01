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
        elif codigo == "20":
            quantidade = int(input("Quantidade de entrada: "))
            caneta = caneta + quantidade
            print("Atualizada quantidade em estoque, estoque atual é:", caneta)