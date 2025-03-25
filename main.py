#Projeto: Jogo de Pedra, Papel e Tesoura

import random

opcoes = {"1" : "Pedra", "2" : "Papel", "3" : "Tesoura"}
vencedor = {"Pedra" : "Tesoura", "Papel" : "Pedra", "Tesoura" : "Papel"}

escolha_computador = random.choice(list(opcoes.values()))

escolha_jogador = input("[1] Pedra \n[2] Papel \n[3] Tesoura \nQual opção você escolhe? \nResposta: ")

if escolha_jogador not in opcoes:
    print("Escolha uma opção válida.")

else:
    escolha_jogador = opcoes[escolha_jogador]

    if escolha_jogador == escolha_computador:
        print("Resultado: Empate!")

    elif vencedor[escolha_jogador] == escolha_computador:
        print("Resultado: Você ganhou!")

    else:
        print("Resultado : Você perdeu!")