import random

class Game:
    classes = ("Mago", "Espadachim", "Berserker")

    def __init__(self, nome, classe):
        self.nome = nome
        self.nivel = 1
        self.forca = 1
        self.vida = 1
        self.stamina = 1
        if classe not in Game.classes:
            raise ValueError("Classe inválida. Escolha entre Mago, Espadachim ou Berserker.")    
        self.classe = classe

    def stats_classe(self):
        if self.classe == "Mago":
            self.forca = 3
            self.vida = 7
            self.stamina = 15
            self.stamina_maxima = 15
            self.vida_maxima = 7
        elif self.classe == "Espadachim":
            self.forca = 5
            self.vida = 6  
            self.stamina = 12
            self.stamina_maxima = 12
            self.vida_maxima = 6
        else:
            self.forca = 4 
            self.vida = 10
            self.stamina = 14
            self.stamina_maxima = 14
            self.vida_maxima = 10

    def ganho_nivel(self):
        forca_antiga = self.forca
        vida_antiga = self.vida
        stamina_antiga = self.stamina
        vida_antiga = self.vida
            
        self.nivel += 1
        self.forca += 2
        self.vida += 3
        self.stamina += 5
        self.stamina_maxima += 5
        self.vida_maxima += 3
        


        print("═" * 60)
        
        if self.nivel <= 5:
            print(f"🎯 Você realmente está evoluindo, fracassado! Você alcançou o nivel {self.nivel}.")
        elif self.nivel > 5 and self.nivel <= 10:
            print(f"🎯 Você está se saindo bem, mas ainda é um fracassado! Você alcançou o nivel {self.nivel}.")
        else:
            print(f"🎯 Quem diria que você fosse chegar até aqui, o admiro garoto. Você conseguiu ultrapassar os limites do jogo e está acima do nivel máximo. Um verdadeiro prodígio entre os fracassados. Alegre-se, você se tornou uma lenda!")

        print("─" * 40)
        print(f"💪 Força: {forca_antiga} → {self.forca} (+2)")
        print(f"❤️  Vida: {vida_antiga} → {self.vida} (+3)")
        print(f"⚡ Stamina: {stamina_antiga} → {self.stamina} (+5)")
        print("═" * 60)

    def ataques(self):
        if self.classe == "Mago":
            self.ataques_info = {
            "Bola De Fogo": {"stam": 3, "dano": 2 + self.forca},
            "Raio Congelante": {"stam": 4, "dano": 3 + self.forca},
            "Tempestade Arcana": {"stam": 6, "dano": 4 + self.forca}
            }
            self.ataques = list(self.ataques_info.keys())
        
        elif self.classe == "Espadachim":
            self.ataques_info = {
            "Corte Rapido": {"stam": 2, "dano": 1 + self.forca},
            "Investida": {"stam": 3, "dano": 2 + self.forca},
            "Shishi Sonson": {"stam": 5, "dano": 3 + self.forca}
            }
            self.ataques = list(self.ataques_info.keys()) 
        
        elif self.classe == "Berserker":
            self.ataques_info = {
                "Golpe Brutal": {"stam": 4, "dano": 3 + self.forca},
                "Fúria Selvagem": {"stam": 5, "dano": 4 + self.forca},
                "Terremoto": {"stam": 7, "dano": 5 + self.forca}
            }
            self.ataques = list(self.ataques_info.keys())

    def descansar(self):
        self.stamina = self.stamina_maxima
        self.vida = self.vida_maxima
        

    def begin(self):
        print("╔" + "═" * 58 + "╗")
        print(f"║{'SWORD ART ONLINE - INÍCIO DA JORNADA':^58}║")
        print("╚" + "═" * 58 + "╝")
        
        print(f"🎮 Jogador: {self.nome}")
        print(f"🏹 Classe: {self.classe}")
        print(f"📊 Nível: {self.nivel}")
        print(f"💪 Força: {self.forca}")
        print(f"❤️  Vida: {self.vida}")
        print(f"⚡ Stamina: {self.stamina}")
        
        print("\n" + "─" * 60)
        print("📋 AVISOS NECESSÁRIOS PARA SUA SOBREVIVÊNCIA:")
        print("🔸 1- Você deve sempre estar atento aos seus arredores, inimigos podem surgir a qualquer momento.")
        print("🔸 2- Sempre gerencie bem sua stamina, ataques mais fortes consomem mais stamina, caso sua stamina chegue a zero, você morrerá instantaneamente.")
        print("🔸 3- Procure sempre evoluir seu nivel, com o nivel sendo aumentado, seus atributos também subirão, isso irá facilitar sua jornada.")
        print("🔸 4- Divirta-se ou morra!")
        print("─" * 60)

    def parte2(self):
        print("\n" + "╔" + "═" * 58 + "╗")
        print(f"║{'CAPÍTULO 2: A DUNGEON DOS GOBLINS':^58}║")
        print("╚" + "═" * 58 + "╝")
        
        print("🌄 Após alguns dias explorando o mundo de Aincrad, você se sente mais confiante.")
        print("🏔️  Após vagar dias, você avista outra dungeon ao longe, decidindo se aproximar dela.")
        print("👹 Ao chegar perto, você percebe que a entrada está cercada por goblins que parecem estar protegendo algo.")
        print("🔊 Você sabe que enfrentá-los será um desafio, mas parece ter uma voz vindo de dentro da dungeon, o chamando para entrar.")
        print("💀 Você precisa entrar lá.")
        print("\n" + "─" * 60)
        print("🎯 Então fracassado, agora é seu momento!")
        print("💨 Respire e vá a batalha contra esses goblins nojentos!")
        print("🔍 Descubra cada vez mais sobre esse mundo!")
        print("─" * 60)
        print("🎯 Essa é a primeira e última vez que irei encorajá-lo a enfrentar alguém,")
        print("💔 então não me decepcione fracassado!")
        print("🔮 Essa dungeon tem algo de especial,")
        print("😈 eu quero que você derrote-os e descubra o que está lá HAHAHAHA!")
        print("─" * 60)