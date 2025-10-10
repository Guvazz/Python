def classificacaoInmetro(inmetro):
    if inmetro == "A":
        print("Muito Eficiente")
    elif inmetro == "B":
        print("Eficiente")
    elif inmetro == "C":
        print("Pouco Eficiente")
    elif inmetro == "D":
        print("Ineficiente")
    else:
        print(f"Inmetro {inmetro} não encontrado")


def main():
    print("Digite uma letra de A até D")
    inmetro = input()
    classificacaoInmetro(inmetro)


if __name__ == "__main__":
    main()