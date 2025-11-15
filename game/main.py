from player import Game
from battles import desafio_inicial, batalha_goblins

def main():

    # Jogo Parte 1
    jogo1 = Game("Tatuir", "Berserker")
    jogo1.stats_classe()
    jogo1.ataques()
    jogo1.begin()
    desafio_inicial(jogo1)

    # Jogo Parte 2
    jogo1.parte2()
    batalha_goblins(jogo1)

    # Jogo Parte 3
    jogo1.parte3()

    # Jogo Parte 4
    jogo1.parte4()  # ← ADICIONAR ESTA LINHA
    
if __name__ == "__main__":
    main()