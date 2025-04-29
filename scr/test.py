from main import *

def test_empate():
    assert decidir_resultado("Pedra", "Pedra") == "Empate"
    assert decidir_resultado("Papel", "Papel") == "Empate"
    assert decidir_resultado("Tesoura", "Tesoura") == "Empate"

def test_ganhou():
    assert decidir_resultado("Pedra", "Tesoura") == "Ganhou"
    assert decidir_resultado("Papel", "Pedra") == "Ganhou"
    assert decidir_resultado("Tesoura", "Papel") == "Ganhou"

def test_perdeu():
    assert decidir_resultado("Pedra", "Papel") == "Perdeu"
    assert decidir_resultado("Papel", "Tesoura") == "Perdeu"
    assert decidir_resultado("Tesoura", "Pedra") == "Perdeu"