    #faça um programa que receba um vetor de 5 números inteiros 
lista = [1,3,5,7,9]
print("O Maior número é: ", max(lista))
print("O Menor número é: ", min(lista))
print("A quantidade de números na lista é: ", len(lista))
print("A soma dos números é: ", sum(lista))

#Mostra quantas vezes o número 1 apareceu
lista = [1,2,1,5,6,4,3,1]
print(lista.count(1))

#Faça um programa que receba um vetor de 5 frutas, mostre-os. Depois, substitua o segundo elemento do vetor por Laranja
lista = ["abacaxi", "maçã", "uva", "pêra", "goiaba"]
print(lista)
lista[1:2] = ["Laranja"]
print(lista)