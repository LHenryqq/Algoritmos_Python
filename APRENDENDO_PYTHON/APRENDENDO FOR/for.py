# # frutas = ["maçã","banana","laranja","manga","pêra"]
# # for i in frutas:
# #     print(i)
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
for i in range(2,200,1):
    print("_______________")
    for j in range(1,11):
        print(i,"x",j,"=",i*j)