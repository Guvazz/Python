def verificaDivisibilidade(numero):
    divisivel_por_2 = (numero % 2 == 0)
    divisivel_por_3 = (numero % 3 == 0)

    if divisivel_por_2 and divisivel_por_3:
        print(f"O número {numero} é divisível por 2 e 3.")
    else:
        print(f"O número {numero} não é divisível por 2 e 3.")


numero = int(input("Digite um número inteiro: "))
verificaDivisibilidade(numero)
