def computador_escolhe_jogada(n, m):
    jogada = min(m, n)

    if n % (m + 1) != 0:
        jogada = n % (m + 1)

    return jogada


def usuario_escolhe_jogada(n, m):
    jogada = 0

    while jogada < 1 or jogada > min(m, n):
        try:
            jogada = int(input("Quantas peças você vai tirar? "))

            if jogada < 1 or jogada > min(m, n):
                raise ValueError

        except ValueError:
            print("Jogada inválida. Tente novamente.")

    return jogada


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
        vez = 1
    else:
        print("Computador começa!")
        vez = 0

    while n > 0:
        if vez == 1:
            jogada = usuario_escolhe_jogada(n, m)
            print("Você tirou", jogada, "peça(s).")
            vez = 0
        else:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou", jogada, "peça(s).")
            vez = 1

        n -= jogada

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        elif n > 1:
            print("Agora restam", n, "peças no tabuleiro.")

    if vez == 0:
        print("Fim do jogo! Você ganhou!")
        return 0
    else:
        print("Fim do jogo! O computador ganhou!")
        return 1


def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for _ in range(3):
        print("=== Partida ===")
        vencedor = partida()

        if vencedor == 1:
            placar_usuario += 1
        else:
            placar_computador += 1

        print("=== Fim da Partida ===\n")

    print("=== Placar Final ===")
    print(f"Você {placar_usuario} X {placar_computador} Computador")


print("Bem-vindo ao jogo do NIM!\n")

opcao = int(input("Escolha:\n1 - Jogar partida única\n2 - Jogar campeonato\n"))

if opcao == 1:
    print("\n=== Partida Única ===")
    partida()
elif opcao == 2:
    print("\n=== Campeonato ===")
    campeonato()
else:
    print("Opção inválida.")
