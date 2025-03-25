#Projeto: Jogo de Pedra, Papel e Tesoura

import random

opcoes = {"1" : "Pedra", "2" : "Papel", "3" : "Tesoura"}
escolha_computador = random.choice(list(opcoes.values()))

escolha_jogador = input("[1] Pedra \n [2] Papel \n [3] Tesoura \n Qual opção você escolhe? \n")

if escolha_jogador == opcao_pedra and escolha_computador == "Pedra":
    print("Sua escolha: Pedra \n" + "Escolha_do_computador" + escolha_computador + "\nResultado: Empate!")

if escolha_jogador == opcao_pedra and escolha_computador == "Papel":
    print("Sua escolha: Pedra \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Você perdeu!")

if escolha_jogador == opcao_pedra and escolha_computador == "Tesoura":
    print("Sua escolha: Pedra \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Você ganhou!")


if escolha_jogador == opcao_papel and escolha_computador == "Pedra":
    print("Sua escolha: Papel \n" + "Escolha do computador: " + escolha_computador + "\nResultado: Você ganhou!")

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