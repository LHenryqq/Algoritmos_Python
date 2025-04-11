#Verificar letra
# sexo = str(input("Digite a letra do seu sexo: ")).upper()
# if sexo == "F":
#     print("Feminino")
# elif sexo == "M":
#     print("Masculino")
# elif sexo == "O":
#     print("Outros")
# else:
#     print("Sexo inválido")

#Verificar se é letra ou consoante
# letra = str(input("Digite uma letra: ")).upper()
# if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
#     print("Vogal")
# else:
#     print("Consoante")

#Lê 3 números e mostre o maior
# num_1 = input("Digite um número: ")
# num_2 = input("Digite mais um número: ")
# num_3 = input("Digite mais um número: ")
# if num_1 > num_2 > num_3:
#     print("O maior número é o primeiro:", num_1)
#     print("O menor número é o terceiro:", num_3)
# elif num_1 > num_3 > num_2:
#     print("O maior número é o primeiro:", num_1)
#     print("O menor número é o segundo:", num_2)
# elif num_2 > num_1 > num_3:
#     print("O maior número é o segundo:", num_2)
#     print("O menor número é o terceiro:", num_3)
# elif num_2 > num_3 > num_1:
#     print("O maior número é o segundo:", num_2)
#     print("O menor número é o primeiro:", num_1)
# elif num_3 > num_1 > num_2:
#     print("O maior número é o terceiro:", num_3)
#     print("O menor número é o segundo:", num_2)
# elif num_3 > num_2 > num_1:
#     print("O maior número é o terceiro:", num_3)
#     print("O menor número é o primeiro:", num_1)
# else:
#     print("Números iguais")

# prod_1 = float(input("Digite o valor do produto 1: "))
# prod_2 = float(input("Digite o valor do produto 2: "))
# prod_3 = float(input("Digite o valor do produto 3: "))
# if prod_1 < prod_2 and prod_1<prod_3:
#     print("Comprar o produto 1")
# elif prod_2 < prod_3 and prod_2 < prod_1:
#     print("Comprar o produto 2")
# elif prod_3 < prod_2 and prod_3 < prod_1:
#     print("Comprar o produto 3")
# else:
#     print("Compre o que você mais gostou")

#leir números e colocá-los em ordem decrescente
# num_1 = float(input("Digite um número: "))
# num_2 = float(input("Digite mais um número: "))
# num_3 = float(input("Digite mais um número: "))
# if num_1 > num_2 and num_2 > num_3:
#     print(num_1, ",", num_2, ",", num_3)
# elif num_1 > num_3 and num_3 > num_2:
#     print(num_1, ",", num_3, ",", num_2)
# elif num_2 > num_1 and num_1 > num_3:
#     print(num_2, ",", num_1, ",", num_3)
# elif num_2 > num_3 and num_3 > num_1:
#     print(num_2, ",", num_3, ",", num_1)
# elif num_3 > num_1 and num_1 > num_2:
#     print(num_3, ",", num_1, ",", num_2)
# elif num_3 > num_2 and num_2 > num_1:
#     print(num_3, ",", num_2, ",", num_1)


salario = float(input("Digite o valor do salário: R$"))
if salario <= 280.55:
    porcent = 22.51
    reajuste = salario*(porcent / 100)
elif salario >= 280.56 and salario <= 709.72:
    porcent = 15.39
    reajuste = salario*(porcent / 100)
elif salario >= 709.73 and salario <= 1501.33:
    porcent = 10.97
    reajuste = salario*(porcent / 100)
else:
    porcent = 5.19
    reajuste = salario*(porcent / 100)
salario_atual = salario + reajuste
print("O Salário inicial era: R$", salario)
print("A porcentagem do reajuste é:", porcent,"%")
print("A correção que deve ser feita é de: R$%.2f"%reajuste)
print("O Salário com o reajuste será de: R$%.2f"%salario_atual)