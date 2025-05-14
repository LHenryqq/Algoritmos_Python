#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
n = int(input("Digite o número de termos da série de Fibonacci: "))
sequencia = []
ultimoNumero = 0
numeroAnterior = 1
for count in range(n):
    proximoNumero = ultimoNumero + numeroAnterior
    sequencia.append(proximoNumero)
    ultimoNumero = numeroAnterior
    numeroAnterior = proximoNumero

print("Série de Fibonacci:", sequencia)
