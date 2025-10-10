def apresentajogador(opcao):
    match opcao:
        case 1:
            print(f"jogador 1: bento")
        case 2:
            print(f"jogador 2: vitinho")
        case 3:
            print(f"jogador 3: gabriel")
        case 4:
            print(f"jogador 4: eder militao")
        case 5:
            print(f"jogador 5: casemiro")
        case 6:
            print(f"jogador 6: douglas santos")
        case 7:
            print(f"jogador 7: vinicius jr")
        case 8:
            print(f"jogador 8: bruno guimares")
        case 9:
            print(f"jogador 9: richarlison")
        case 10:
            print(f"jogador 10: rodrygo")
        case 11:
            print(f"jogador 11: paqueta")
        case _:
            print(f"jogador {opcao} nao encontrado")


def main():
    print("digite um numero de camisa de 1 ate 11:")
    opcao = int(input())

    apresentajogador(opcao)
if __name__ == "__main__":
    main()