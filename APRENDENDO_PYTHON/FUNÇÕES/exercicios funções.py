# # Crie uma função que receba um nome e imprima uma saudação personalizada.
# def saudacao(nome):
#     print(f"Olá {nome}, bem vindo!!!")
# nome = input("Nickname: ")
# saudacao(nome)

# # Crie uma função que receba dois números e retorne sua soma.
# def soma(x,y):
#     add = x + y
#     print(add)
# a = float(input("Primeiro número: "))
# b = float(input("Segundo número: "))
# soma(a,b)

# # Escreva uma função que calcule o quadrado de um número.
# def quadrado(num):
#     calculo = num ** 2
#     print(calculo)
# valor = float(input("Digite um número: "))
# quadrado(valor)

# # Escreva uma função que verifique se um número é par.
# def par(num):
#     verific = num % 2
#     if verific == 0:
#         print("Número é par.")
#     else:
#         print("Número é ímpar.")
# numero = float(input("Número: "))
# par(numero)

# # Escreva uma função que receba uma lista de números e retorne o maior elemento.
# lista_numeros = [80, 5, 30, 52, 50]
# def maior(lista):
#     lista.sort()
#     print("Maior número:", lista[-1])
# maior(lista_numeros)

# # Crie uma função que calcule o fatorial de um número (sem usar recursão).
# def fatorial(num):
#     result = 1
#     for i in range(num):
#         if num > 1: 
#             result = result * num
#             num = num-1
#         else:
#             print(f"Resultado: {result}")
#             break
# fat = int(input("Número fatorial: "))
# fatorial(fat)

# # Crie uma função que receba um número e retorne True se ele for primo.
# def primo(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
# numero = int(input("Digite um número para verificar se é primo: "))
# print(primo(numero))
        

# Crie uma função que inverta uma string.

# Crie uma função que receba uma lista de nomes e retorne apenas os nomes com mais de 5 letras.

# Escreva uma função que conte quantas vogais há em uma string.

# Crie uma função que receba um número e retorne uma lista com todos os divisores dele.

# Crie uma função que converta graus Celsius para Fahrenheit.

# Crie uma função que receba uma string e retorne a mesma string sem espaços.

# Crie uma função que receba uma lista e retorne a média dos elementos.

# Escreva uma função que receba uma palavra e retorne True se ela for um palíndromo.

# Crie uma função que gere uma lista com os n primeiros números pares.

# Escreva uma função que receba um número e retorne a tabuada dele (de 1 a 10).

# Crie uma função que calcule a área de um retângulo (base × altura).

# Crie uma função que retorne o menor valor entre três números.

# Escreva uma função que simule o lançamento de um dado de 6 faces (use random.randint).