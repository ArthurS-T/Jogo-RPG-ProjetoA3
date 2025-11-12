from player import Game
from battles import desafio_inicial, batalha_goblins

def main():

    #Jogo Parte 1
    jogo1 = Game("Kirito", "Espadachim") #Escolha seu nome e sua classe aqui. Classes (Mago, Espadachim, Berserker)
    jogo1.stats_classe()
    jogo1.ataques()
    jogo1.begin()
    desafio_inicial(jogo1)

    #Jogo Parte 2
    jogo1.parte2()
    batalha_goblins(jogo1)

    #Jogo Parte 3
    
if __name__ == "__main__":
    main()