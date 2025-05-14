#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto 
#indeterminado de temperatura, bem como o mês e o ano que ocorreu essa temperatura, e informe ao final a menor 
#e a maior temperaturas informadas, o mês e o ano em que elas ocorreram, bem como a média de todas as 
#temperaturas.
maior = float("-inf")
menor = float("inf")
temperaturas = 0
num_registros = int(input("Qual o número de registros que deseja realizar: "))
for i in range(num_registros):
    mes = int(input("Mês do registro: "))
    if mes < 1 and mes > 12:
        print("Digite um mês válido.")
    ano = int(input("Ano do registro: "))
    temp = float(input("Qual a temperatura: "))
    temperaturas = temperaturas + temp
    if temp >= maior:
        maior = temp
        result_maior = (f"{mes}/{ano} : temperatura de {temp}°C")
    if temp <= menor:
        menor = temp
        result_menor = (f"{mes}/{ano} : temperatura de {temp}°C")
media_temp = temperaturas/num_registros
print(f"A temperatura média é: {media_temp}")
print(f"Maior Temperatura registrada: {result_maior}")
print(f"Menor Temperatura registrada: {result_menor}")