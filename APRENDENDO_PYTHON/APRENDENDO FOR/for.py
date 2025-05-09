# frutas = ["maçã","banana","laranja","manga","pêra"]
# for i in frutas:
#     print(i)
# frutas = "banana"
# for i in frutas:
#     print(i)

# nomes = ["Pedro", "João","Letícia"]
# for n in nomes:
#     if n == "João":
#         continue
#     print(n)

#O primeiro número é por onde ele começa a contar, e o último é até onde ele conta -1. (APENAS NÚMEROS INTEIROS)
# inicio = int(input("Digite um número: "))
# fim = int(input("Digite um número: "))
# for x in range(inicio,fim):
#     print(x)

#O terceiro número define o intervalo da contagem
# inicio = int(input("Digite o início: "))
# intervalo = int(input("Digite o intervalo: "))#incremento (intervalo positivo), decremento(intervalo negativo).
# fim = int(input("Digite o fim: "))
# fim = fim+intervalo #somando o intervalo, faz ele contar todos os números de acordo com o intervalo escolhido até o número final escolhido.
# for x in range(inicio,fim,intervalo):
#     print(x)

#for aninhado. (repete até escrever todas as formas)
# for i in range(5):
#     for j in range(6):
#         print(i,j)

#Tabuada
# for i in range(1,11,1):
#     print("_______________")
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)

#imprime apenas números ímpares de 1 a 50
# for i in range(1,50,2):
#     print(i)

#printar times enumerados
# times = ["Palmeiras","Flamengo","São Paulo"]
# for i in range(len(times)):
#     print(f"{i+1}- {times[i]}")

# print("Digite dois números e descubra os números inteiros do intervalo entre eles")
# inicio = int(input("Início do intervalo: "))
# fim = int(input("Digite o número final: "))
# intervalo = int(input("Qual o intervalo entre números: "))
# for i in range(inicio+intervalo, fim, intervalo):
#     print(i)
#     soma = sum(range(inicio+intervalo, fim, intervalo))
# print("O resultado da soma dos números do intervalo é:",soma)

# for i in range(1,21):
#     print(i,end=" ",)

#Somar números
# soma=0
# acumulador = 0
# for i in range(5):
#     num1 = int(input("Digite um valor: "))
#     soma = soma + num1 #acumulador  
#     acumulador = acumulador + 1
# media = soma / acumulador
# print("A média é: ", media)

#N NÚMEROS, SOMA DOS NÚMEROS, EXIBE O MAIOR E O MENOR
maior = float("-inf")
menor = float("inf")
n = int(input("Quantidade de números na conta:"))
soma = 0
acumulador = 0
for i in range(n):
    num = int(input("Digite um valor: "))
    if num < 0:
        print("O número deve ser positivo.")
    soma = soma + num 
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma dos números é: {soma}")