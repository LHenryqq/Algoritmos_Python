#MÉDIA DE IDADE DA TURMA
# pessoas = int(input("Quantidade de pessoas na turma: "))
# idades = 0
# for i in range(pessoas):
#     idade = int(input("Digite a idade: "))
#     idades = idades + idade
# media_idade = (idades) / pessoas
# if media_idade >= 0 and media_idade <= 25:
#     print("Turma Jovem")
# elif media_idade >= 26 and media_idade <= 60:
#     print("Turma Adulta")
# elif media_idade > 60 and idade <= 100:
#     print("Turma Idosa")
# else:
#     print("Idade inválida.")
# print(f"A média de idade na turma é de {media_idade}")

#ELEIÇÃO
resultado = 0
contador = 0
vencedor = 0
eleitores = int(input(" Quantidade de eleitores: "))
cand_1 = input("Nome do Candidato 1: ")
num_cand1 = int(input("Número do candidato 1: "))
vence_1 = 0
cand_2 = input("Nome do Candidato 2: ")
num_cand2 = int(input("Número do candidato 2: "))
vence_2 = 0
cand_3 = input("Nome do Candidato 3: ")
num_cand3 = int(input("Número do candidato 3: "))
vence_3 = 0
print(f"Para votar no candidato {cand_1}, digite {num_cand1}")
print(f"Para votar no candidato {cand_2}, digite {num_cand2}")
print(f"Para votar no candidato {cand_3}, digite {num_cand3}")
for i in range(eleitores):
    voto = int(input("Número do voto: "))
    if voto == num_cand1 or voto == num_cand2 or voto == num_cand3:
        print("Voto computado.")
    else:
        print("Voto inválido. Digite o número de um dos candidatos.")
        if voto == num_cand1:
            vence_1 = vence_1 + 1
        elif voto == num_cand2:
            vence_2 = vence_2 + 1
        elif voto == num_cand3:
            vence_3 = vence_3 + 1
        else:
            print("Número de candidato inválido.")
print("Resultados: ")
print(f"{cand_1}: {vence_1} votos. \n{cand_2}: {vence_2} votos.\n{cand_3}: {vence_3} votos.")
if vence_1 > vence_2 and vence_1 > vence_3 and vence_2 > vence_3:
    print(f"Candidato {cand_1} venceu as eleições com {vence_1} votos.")
    vencedor = vence_1
    segundo = vence_2
elif vence_1 > vence_2 and vence_1 > vence_3 and vence_3 > vence_2:
    print(f"Candidato {cand_1} venceu as eleições com {vence_1} votos.")
    vencedor = vence_1
    segundo = vence_3
elif vence_2 > vence_1 and vence_2 > vence_3 and vence_3 > vence_1:
    print(f"Candidato {cand_2} venceu as eleições com {vence_2} votos.")
    vencedor = vence_2
    segundo = vence_3
elif vence_2 > vence_1 and vence_2 > vence_3 and vence_1 > vence_3:
    print(f"Candidato {cand_2} venceu as eleições com {vence_2} votos.")
    vencedor = vence_2
    segundo = vence_1
elif vence_3 > vence_1 and vence_3 > vence_2 and vence_2 > vence_1:
    print(f"Candidato {cand_3} venceu as eleições com {vence_3} votos.")
    vencedor = vence_3
    segundo = vence_2
elif vence_3 > vence_1 and vence_3 > vence_2 and vence_1 > vence_2:
    print(f"Candidato {cand_3} venceu as eleições com {vence_3} votos.")
    vencedor = vence_3
    segundo = vence_1
if vencedor == segundo:
    print("Empate.")