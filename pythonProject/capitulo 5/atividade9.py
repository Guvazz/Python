def verificaDivisibilidade(numero):
    divisivel_por_5 = numero % 5 == 0
    divisivel_por_3 = numero % 3 == 0

    if divisivel_por_5 or divisivel_por_3:
        print(f"O número {numero} é divisível por 5 ou 3.")
    else:
        print(f"O número {numero} não é divisível por 5 nem por 3.")

numero = int(input("Digite um número inteiro: "))
verificaDivisibilidade(numero)
