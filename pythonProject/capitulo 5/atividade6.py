def checa_par_ou_impar(num):
    if num % 2 != 1:
        print("O número é par.")
    else:
        print("O número é ímpar.")

valor = int(input("Informe um número: "))

checa_par_ou_impar(valor)
