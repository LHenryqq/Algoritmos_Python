#listas mutáveis

#alterar elementos
frutas = ["banana", "maça","cereja"]

frutas[0] = "pera"
frutas[-1] = "laranja"
print(frutas)

uma_lista = ["a", "b", "c", "d", "e", "f"]
uma_lista[1:3] = ["x", "y"]
print(uma_lista)

#remover elementos
uma_lista = ["a", "b", "c", "d", "e", "f"]
print(uma_lista)
print(len(uma_lista))
uma_lista[1:3] = []
print(uma_lista)
print(len(uma_lista))

#inserir elementos
uma_lista = ["a", "d", "f"]
uma_lista[1:1] = ["b", "c"]
print(uma_lista)
uma_lista[4:4] = ["e"]
print(uma_lista)

#remover eficiente (del)
a = ["um", "dois", "três"]
del a[1]
print(a)

lista = ["a", "b","c", "d","e","f"]
del lista[1:5]
print(lista)