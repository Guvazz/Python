def verificaNumero(numero):
    if numero != 0:
        if numero > 0:
            print("O número é positivo.")
        else:
            print("O número é negativo.")
    else:
        print("É ZERO")

numero = int(input("Digite um número: "))
verificaNumero(numero)
