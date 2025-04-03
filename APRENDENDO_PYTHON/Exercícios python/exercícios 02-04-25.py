#Exercício listas
lista = [0,1,2,3,4,5,6,7,8,9,10]

print(lista[1:10]) #imprimir 1 ao 10
print(lista[8:]) #imimir 8 ao 10
print(lista[2:10:2]) #imprimir números pares (salto-> [2(início do salto):10(Quantidade de elementos que abrange),2(Distância do salto)])
print(lista[1:10:2]) #imprimir números ímpares
lista.sort(reverse = True) #imprimir lista reversa
print(lista) #imprimir lista reversa

#Exercício notas
notasP1 = [7.0, 8.3, 10.0, 6.5, 9.3]
notasP2 = [8.5, 6.9, 5.0, 7.5, 9.8]
mediaP1 = (sum(notasP1) / len(notasP1))
mediaP2 = (sum(notasP2) / len(notasP2))
print("A média da turma na prova 1 é: ", mediaP1)
print("A média da turma na prova 2 é: ", mediaP2)