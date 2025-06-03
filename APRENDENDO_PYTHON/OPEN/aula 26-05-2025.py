#Ler
# f = open("APRENDENDO_PYTHON/OPEN/file.txt","r") #"r" é para a função Read, tem apenas permissão para ler.
# print(f.read())
# f.close()#fecha o arquivo após executar

#Acrescentar/escrever
# z = open("APRENDENDO_PYTHON/OPEN/file.txt","a", encoding="utf-8") #"a" - Acrescentar - abre um arquivo para acrescentar. (encoding="utf-8")-> permite caracteres especiais"ç""á"
# x = input("Digite seu nome = ")
# z.write(f"\n{x}")
# z = open("APRENDENDO_PYTHON/OPEN/file.txt","r",encoding="utf-8")
# print(z.read())
# z.close()

#Sobrescrever (apaga o conteúdo anterior e escreve o que for apresentado.)
# f= open("file.txt","w")

# #Criar arquivo
# f = open("file.txt","x")

#Especificar a leitura entre texto ou binário // rb = ler em binário // rt = ler texto
f = open("APRENDENDO_PYTHON/OPEN/download.png","rb")
print(f.read())
f.close()