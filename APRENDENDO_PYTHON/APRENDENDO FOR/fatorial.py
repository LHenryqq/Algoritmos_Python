#CALCULADORA DE FATORIAL
num = int(input("Número fatorial: "))
num_escolhido = num
result = 1
for i in range(num):
    if num > 1: 
        result = result * num
        num = num-1
    else:
        break
print(f"O resultado de {num_escolhido}! é: {result}")