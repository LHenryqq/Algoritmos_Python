#TERMO GERAL DA PG
import time
import math
def pg(primeiro_termo, razao, fim):
    result = primeiro_termo
    inicio = time.time_ns()
    result = primeiro_termo*razao**(fim-1)
    termino = time.time_ns()
    tempo = termino-inicio
    #print("Tempo de execução:", tempo)
    return result

#SOMA PG
def soma_pg_finita(primeiro_termo, razao, fim):
    soma_finita = (primeiro_termo*(1-razao**fim))/(1-razao)#pg FINITA
    return soma_finita

def soma_pg_inf(primeiro_termo, razao):
    #print(2,7)
    soma_inf = (primeiro_termo)/(1-razao)
    return soma_inf

#PRODUTO DOS TERMOS DE UMA PG
def prod_pg(primeiro_termo, razao, fim):
    prod_fim = (primeiro_termo**fim)*(razao**((fim*(fim-1))/2))
    return prod_fim

#n ésimo termo
# def n_pg(a1,q,result):
#     n = (math.log(result)/(math.log(a1*q)))+1
#     return n #ERRO

#print("Termo:", n_pg(100,20,3200))
#exercicio 1
#print(pg(2,2,10))

#exercicio 2
#print(soma_pg_finita(1,2,9))

#exercício 4
tempo = 0
for i in range (1,7):
    tempo += 20
    print(f"Tempo: {tempo}\nCélulas: {pg(100,2,i)}")