# tradutor = {}
# tradutor ["pineapple"] = "abacaxi"
# tradutor ["apple"] = "maça"
# tradutor ["orange"] = "laranja"
# print(type(tradutor))
# print(tradutor)

# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(type(tradutor1))
# print(tradutor1)

#pesquisar valor correspondente
# tradutor1 = {}
# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1["apple"])

#deletar elemento (usando del) del()
# tradutor1 = {}
# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# del (tradutor1 ["apple"])
# print(tradutor1)

#deletar elemento (usando pop(explica quando não encontrou ou exibe o elemento retirado)) .pop()
# tradutor1 = {}
# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# print(tradutor1.pop("orange","Fruta não encontrada"))#o texto após a vírgula é exibido caso não encontre o que se pediu, o primeiro texto exibe o que foi retirado.
# print(tradutor1.pop("banana","Fruta não encontrada"))#exemplo de quando não encontra o que foi pedido.
# print(tradutor1)

#remove todos os elementos do dicionário. .clear()
# tradutor1 = {}
# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# tradutor1.clear()#apaga o dicionário
# print(tradutor1)

#comando "in" retorna como verdadeiro ou falso
# tradutor1 = {}
# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print("pineapple" in tradutor1)

#imprime valores do dicionário. .values()
# tradutor1 = {}
# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print("laranja" in tradutor1.values())#verifica os "resultados" -> "abacaxi", "maça", "laranja"
# print(tradutor1.values())

#substituir valores
# tradutor1 = {}
# tradutor1 = {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# tradutor1["apple"] = "goiaba" #substitui o resultado "maçã" por "goiaba".
# print(tradutor1)

#dicionário de dicionário
# dados = {
#     "Crossfox": {"KM": 35000, "Ano": 2005}, 
#     "DS5": {"KM": 17000,"Ano":2015},
#     "Fusca": {"KM": 130000,"Ano": 1979}, 
#     "Jetta":{"KM":56000,"Ano":2011}, 
#     "Passat": {"KM": 62000,"Ano":1999}
# }

# print(dados["Fusca"]["Ano"])

#funciona como o .pop(), mas não remove o valor, apenas verifica se está no dicionário e imprime o conteúdo
# dados = {
#     "Crossfox": {"KM": 35000, "Ano": 2005}, 
#     "DS5": {"KM": 17000,"Ano":2015},
#     "Fusca": {"KM": 130000,"Ano": 1979}, 
#     "Jetta":{"KM":56000,"Ano":2011}, 
#     "Passat": {"KM": 62000,"Ano":1999}
# }

# print(dados.get("Gol","Veículo não encontrado"))#o primeiro texto é o produto procurado, o segundo texto é o que será exibido caso não encontre o produto procurado.