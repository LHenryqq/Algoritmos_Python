# a = int(input("Digite um número para ser subtraído: "))
# contador = 0
# if a > 0:
#     while a > 0:
#         a = a - 1
#         print(a)
#         contador = contador + 1
#     print("Foi subtraído 1 do número", contador,"vezes até chegar em 0")
# elif a < 0:
#     while a < 0:
#         a = a + 1
#         print(a)
#         contador = contador + 1
#     print("Foi somado 1 ao número", contador,"vezes até chegar em 0")
# else:
#     print("Seu número já é 0")

#FAZER CALCULADORA

# while True:
#     funcao = str(input("Qual função matemática você deseja realizar? M(Multiplicação), D(Divisão), S(Subtração), A(Adição), X(Encerrar) ")).upper()
#     if funcao == "M":
#         funcao = "multiplicação"
#         print("Você selecionou a operação",funcao)
#         num1 = int(input("Digite o primeiro número da operação: "))
#         num2 = int(input("Digite o segundo número da operação: "))
#         result = num1 * num2
#         print("O resultado da",funcao, "é:",result)
#     elif funcao == "D":
#         funcao = "divisão"
#         print("Você selecionou a operação",funcao)
#         num1 = int(input("Digite o primeiro número da operação: "))
#         num2 = int(input("Digite o segundo número da operação: "))
#         result = num1 / num2
#         print("O resultado da",funcao, "é:",result)
#     elif funcao == "S":
#         funcao = "subtração"
#         print("Você selecionou a operação",funcao)
#         num1 = int(input("Digite o primeiro número da operação: "))
#         num2 = int(input("Digite o segundo número da operação: "))
#         result = num1 - num2
#         print("O resultado da",funcao, "é:",result)
#     elif funcao == "A":
#         funcao = "adição"
#         print("Você selecionou a operação",funcao)
#         num1 = int(input("Digite o primeiro número da operação: "))
#         num2 = int(input("Digite o segundo número da operação: "))
#         result = num1 + num2
#         print("O resultado da",funcao, "é:",result)
#     elif funcao == "X":
#         print("Calculadora Encerrada.")
#         break

# while True:
#     nota = float(input("Digite uma nota entre 0 e 10: "))
#     if nota < 0 or nota > 10:
#         print("Valor inválido.")
#     else:
#         break

#nome e senha
# while True:
#     nome = input("Digite o nome de usuário: ").upper()
#     senha = input("Digite uma senha: ").upper()
#     if sorted(senha) == sorted(nome):
#         print("Senha inválida. Não pode conter parte do nome.")
#     else:
#         print("Acesso permitido.")
#         break

#cadastro
while True:
    while True:
        nome = input("Digite seu nome: ").upper()
        if len(nome) < 3:
            print("Erro no nome. O nome deve ter no mínimo 3 caracteres.")
        else:
            break
    while True:
        idade = int(input("Digite sua idade: "))
        if idade < 0 or idade > 150:
            print("Erro na Idade. Digite uma idade válida.")
        else:
            break
    while True:
        salario = float(input("Digite seu salário: R$"))
        if salario <= 0:
            print("Erro no Salário. Digite um salário válido.")
        else:
            break
    while True:
        sexo = input("Digite seu sexo: F(Feminino), M(masculino), O(Outro): ").upper()
        if sexo != "F" and sexo != "M" and sexo != "O":
            print("Erro. Digite um sexo válido.")
        else:
            break
    while True:
        ec = input("Digite seu Estado Civil: S(Solteiro), C(Casado), V(Viúvo(a)), D(Divorciado(a)): ").upper()
        if ec != "S" and ec != "C" and ec != "V" and ec != "D":
            print("Erro. Digite um Estado Civil Válido.")
        else:
            print("Cadastro Concluído.")
        break
    break