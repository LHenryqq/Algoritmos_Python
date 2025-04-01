nome = input("Nome da pessoa: ")
sexo = input("Digite o gênero: ").upper()
idade = int(input("Digite a sua idade: "))

if idade>= 17:
    if sexo == "M":
        print("Obrigatório o alistamento militar!")
    else:
        print("Não é obrigatório se alistar")
else:
    print ("Fora do período de alistamento")