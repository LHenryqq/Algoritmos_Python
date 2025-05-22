try:
    a = int(input("Digite uma palavra: "))
except ValueError:
    print("Digite apenas números inteiros.")
except: 
    print("Erro desconhecido")
finally:
    print("Final do algoritmo")

#NameError:
#4 + spam*3

#SyntaxError:
#while True print('Hello world')

#ZeroDivisionError:
#10 * (1/0)

#TypeError:
#'2' + 2