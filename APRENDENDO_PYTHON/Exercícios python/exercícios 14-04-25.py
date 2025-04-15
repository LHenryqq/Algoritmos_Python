#CALCULAR MÉDIA E APRESENTAR RESULTADO
# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))
# media = (nota1 + nota2)/ 2
# print("A Média é:", media)
# if media >= 7 and media < 10:
#     print("Aprovado")
# elif media >= 10:
#     print("Aprovado com Distinção")
# else:
#     print("Reprovado")

#FOLHA DE PAGAMENTO
horas = float(input("Quantidade de horas trabalhadas: "))
valor = float(input("Valor da hora trabalhada: "))
salario_bruto = horas*valor
print("Salário Bruto: ", "(",horas,"*",valor,") : R$",salario_bruto)
if salario_bruto >= 900 and salario_bruto < 1500:
    ir = salario_bruto*(5/100)
    print("IR = (5%)                : R$", ir)
elif salario_bruto >= 1500 and salario_bruto < 2500:
    ir = (10/100)*salario_bruto
    print("IR = (10%)           : R$", ir)
elif salario_bruto > 2500:
    ir = (20/100)*salario_bruto
    print("IR = (20%)           : R$", ir)
else:
    ir = 0*salario_bruto
    print("IR = (ISENTO)            : R$", ir)
inss = (10/100)*salario_bruto
print("INSS (10%)               : R$", inss)
fgts = (11/100)*salario_bruto
print("FGTS (11%)               : R$", fgts)
descontos = inss + ir
print("Total de Descontos       :", descontos)
salario_liquido = salario_bruto - descontos
print("Salário Líquido          :", salario_liquido)