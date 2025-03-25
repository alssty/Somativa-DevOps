#Projeto: Jogo de Pedra, Papel e Tesoura

import random

opcoes = ["Pedra", "Papel", "Tesoura"]
escolha_computador = random.choice(opcoes)

opcao_pedra = "1"
opcao_papel = "2"
opcao_tesoura = "3"

escolha_jogador = input("[1] Pedra \n"
                            "[2] Papel \n"
                            "[3] Tesoura \n"
                            "Qual opção você escolhe? \n")

if escolha_jogador == opcao_pedra and escolha_computador == "Pedra":
    print("Sua escolha: Pedra \n" + "Escolha_do_computador" + escolha_computador + "\nResultado: Empate!")

if escolha_jogador == opcao_pedra and escolha_computador == "Papel":
    print("Sua escolha: Pedra \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Você perdeu!")

if escolha_jogador == opcao_pedra and escolha_computador == "Tesoura":
    print("Sua escolha: Pedra \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Você gahnou!")


if escolha_jogador == opcao_papel and escolha_computador == "Pedra":
    print("Sua escolha: Papel \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Você gahnou!")

if escolha_jogador == opcao_papel and escolha_computador == "Papel":
    print("Sua escolha: Papel \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Empate!")

if escolha_jogador == opcao_papel and escolha_computador == "Tesoura":
    print("Sua escolha: Papel \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Você perdeu!")


if escolha_jogador == opcao_tesoura and escolha_computador == "Pedra":
    print("Sua escolha: Tesoura \n" + "Escolha do computador: " + escolha_computador + "\nResultado:  Você perdeu!")

if escolha_jogador == opcao_tesoura and escolha_computador == "Papel":
    print("Sua escolha: Tesoura \n" + "Escolha do computador: " + escolha_computador + "\nResultado:  Você ganhou!")

if escolha_jogador == opcao_tesoura and escolha_computador == "Tesoura":
    print("Sua escolha: Tesoura \n" + "Escolha do computador: " + escolha_computador + "\nResultado:  Empate!")