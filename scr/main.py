#Projeto: Jogo de Pedra, Papel e Tesoura

import random

opcoes = {"1" : "Pedra", "2" : "Papel", "3" : "Tesoura"}
vencedor = {"Pedra" : "Tesoura", "Papel" : "Pedra", "Tesoura" : "Papel"}

def escolha_computador():
    return random.choice(list(opcoes.values()))

def decidir_resultado(jogador, computador):
    if jogador == computador:
        return "Empate"
    elif vencedor[jogador] == computador:
        return "Ganhou"
    else:
        return "Perdeu"

def main():

    while True:

        escolha_jogador = input("\n[1] Pedra \n[2] Papel \n[3] Tesoura \nQual opção você escolhe? \nResposta: ")

        if escolha_jogador not in opcoes:
            print("\nEscolha uma opção válida.")
            continue

        jogador = opcoes[escolha_jogador]
        computador = escolha_computador()

        print("\nSua escolha: ", escolha_jogador)
        print("Escolha do computador: ", escolha_computador)

        resultado = decidir_resultado(jogador, computador)
        print(f"Você {resultado}!")

        while True:
            jogar_novamente = input("\nGostaria de jogar novamente? (sim/nao) \nResposta: ")

            if jogar_novamente == "sim":
                break

            if jogar_novamente == "nao":
                print("\nAté mais!")
                exit()

            else:
                print("\nDigite uma opção válida (sim/nao)")

if __name__ == "__main__":
    main()