#Escreva uma fução chamada que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas.
lista = [[1,2],[3],[4,5,6]]
print(sum(lista[0])+sum(lista[1])+sum(lista[2]))

#Escreva uma função chamada que receba uma lista de numeros e retorne a soma cumulativa, ou seja, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos
# da lista original.
lista = [1,2,3]
a = sum(lista[0:1])
b = sum(lista[0:2])
c = sum(lista[0:3])
print([a,b,c])
print([lista[0], lista[0]+lista[1], lista[0]+lista[1]+lista[2]])

#Escreva uma função que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos.
lista = [1,2,3,4]
lista.pop(0)
lista.pop()
print(lista)

#Você precisa adicionar o elemento "Brasil", nos dados abaixo:
country = ["Alemanha", "Itália", "Japão"]
country.extend("Brasil")
print(country)