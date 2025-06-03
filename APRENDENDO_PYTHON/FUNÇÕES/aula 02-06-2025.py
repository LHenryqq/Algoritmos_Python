# def hello(nome):
#     print("Olá!!!", nome)
# a = input("Digite seu nome: ")
# hello(a)
# hello('Ederson')
# hello('João')
# hello('Maria')
# hello('Pedro')
# hello('José')

# def hello(nome, idade):
#     print("Olá!!!", nome, '\nSua idade é:',idade)

# hello("Ederson", 25)

# def calcular_pagamento(qtd_horas, valor_hora):
#     horas = float(qtd_horas)
#     taxa = float(valor_hora)
#     if horas <= 40:
#         salario = horas*taxa
#     else:
#         h_excd = horas-40
#         salario = 40*taxa+(h_excd*(1.5*taxa))
#     print(salario)
# a = float(input("Horas: "))
# b = float(input("Valor da hora: "))
# calcular_pagamento(a,b)


#RETURN (RETORNAR VALOR EM QUALQUER LUGAR QUE ESTEJA NO CÓDIGO)
def soma(x,y):
    result = x+y
    return result
a = int(input("Primeiro Número: "))
b = int(input("Segundo Número: "))
res = soma(a,b)#atribua a uma variável; #a variável "res" chama novamente a função e atribui os valores.
print("Soma:",res)