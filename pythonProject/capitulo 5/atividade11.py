def classificarProduto(codigo):
    if codigo == 1:
        classificacao = "Alimento não-perecível"
    elif codigo in range(2, 5):
        classificacao = "Alimento perecível"
    elif codigo in (5, 6):
        classificacao = "Vestuário"
    elif codigo == 7:
        classificacao = "Higiene pessoal"
    elif 8 <= codigo <= 15:
        classificacao = "Limpeza e utensílios domésticos"
    else:
        classificacao = "Código inválido"

    print(f"Classificação: {classificacao}")


codigo = int(input("Digite o código do produto: "))
classificarProduto(codigo)
