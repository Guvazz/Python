def classificarJogador(idade):
    if idade < 5:
        print("Idade inválida.")
    elif idade <= 7:
        print("Categoria: Infantil A (5 - 7 anos)")
    elif idade <= 10:
        print("Categoria: Infantil B (8 - 10 anos)")
    elif idade <= 13:
        print("Categoria: Juvenil A (11 - 13 anos)")
    elif idade <= 17:
        print("Categoria: Juvenil B (14 - 17 anos)")
    else:
        print("Categoria: Sênior (18 anos ou mais)")

idade = int(input("Digite a idade do jogador: "))
classificarJogador(idade)
