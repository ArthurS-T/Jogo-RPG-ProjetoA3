import time 
import random

import time
import random
import sys

class MinigameTreino:
    def __init__(self):
        self.flexoes_alvo = 100
        self.abdominais_alvo = 50
        self.corrida_alvo = 5  # km
        self.flexoes_feitas = 0
        self.abdominais_feitos = 0
        self.corrida_feita = 0
        self.stamina = 100
        
    def typewriter(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def mostrar_progresso(self):
        print("\n" + "═" * 50)
        print("📊 PROGRESSO DO TREINO:")
        print(f"💪 Flexões: {self.flexoes_feitas}/{self.flexoes_alvo}")
        print(f"🔥 Abdominais: {self.abdominais_feitos}/{self.abdominais_alvo}") 
        print(f"🏃‍♂️ Corrida: {self.corrida_feita:.1f}km/{self.corrida_alvo}km")
        print(f"⚡ Stamina: {self.stamina}%")
        print("═" * 50)
    
    def minigame_flexoes(self):
        print("\n🎯 MINIGAME: FLEXÕES")
        self.typewriter("Pressione 'F' rapidamente para fazer flexões!")
        self.typewriter("Cuidado com a stamina! (Pressione 'Q' para descansar)")
        
        while self.flexoes_feitas < self.flexoes_alvo and self.stamina > 0:
            try:
                tecla = input("\nPressione uma tecla: ").upper()
                
                if tecla == 'F':
                    flexoes_nessa_vez = random.randint(3, 8)
                    self.flexoes_feitas += flexoes_nessa_vez
                    self.stamina -= random.randint(5, 12)
                    
                    if self.stamina < 0:
                        self.stamina = 0
                    
                    print(f"💪 +{flexoes_nessa_vez} flexões! Bom trabalho!")
                    self.mostrar_progresso()
                    
                elif tecla == 'Q':
                    descanso = random.randint(15, 25)
                    self.stamina += descanso
                    if self.stamina > 100:
                        self.stamina = 100
                    print(f"💤 Descansando... +{descanso}% stamina")
                    self.mostrar_progresso()
                    
                else:
                    print("❌ Tecla errada! Use 'F' para flexões ou 'Q' para descansar")
                    
            except KeyboardInterrupt:
                print("\n😴 Treino interrompido...")
                return False
                
        if self.stamina <= 0:
            print("\n💀 Você desmaiou de cansaço! Precisa descansar mais.")
            return False
            
        print("\n✅ FLEXÕES CONCLUÍDAS! Você está mais forte!")
        return True
    
    def minigame_abdominais(self):
        print("\n🎯 MINIGAME: ABDOMINAIS")
        self.typewriter("Acerte a sequência para fazer abdominais!")
        self.typewriter("Digite exatamente o que aparece na tela")
        
        sequencias = ["CRUNCH", "SIT UP", "LEVANTA", "FORCA", "RESPIRA"]
        
        while self.abdominais_feitos < self.abdominais_alvo and self.stamina > 0:
            sequencia = random.choice(sequencias)
            print(f"\n🔤 Digite: {sequencia}")
            
            try:
                resposta = input("Sua resposta: ").upper().strip()
                
                if resposta == sequencia:
                    abdominais_nessa_vez = random.randint(2, 6)
                    self.abdominais_feitos += abdominais_nessa_vez
                    self.stamina -= random.randint(3, 8)
                    
                    if self.stamina < 0:
                        self.stamina = 0
                    
                    print(f"🔥 +{abdominais_nessa_vez} abdominais! Excelente!")
                    self.mostrar_progresso()
                else:
                    print("❌ Errou a sequência! Tente novamente.")
                    self.stamina -= 2
                    
            except KeyboardInterrupt:
                print("\n😴 Treino interrompido...")
                return False
                
        if self.stamina <= 0:
            print("\n💀 Você desmaiou de cansaço!")
            return False
            
        print("\n✅ ABDOMINAIS CONCLUÍDOS! Seu core está mais forte!")
        return True
    
    def minigame_corrida(self):
        print("\n🎯 MINIGAME: CORRIDA")
        self.typewriter("Mantenha pressionado ENTER para correr!")
        self.typewriter("Solte para controlar o pace (Pressione CTRL+C para parar)")
        
        print("\n🏃‍♂️ Preparado... 3... 2... 1... VAI!")
        
        distancia_por_segundo = 0.1  # km por segundo de pressionamento
        start_time = time.time()
        
        try:
            while self.corrida_feita < self.corrida_alvo:
                print(f"\n📏 Distância: {self.corrida_feita:.1f}km / {self.corrida_alvo}km")
                print("🎯 Pressione ENTER para correr (mantenha pressionado)...")
                
                input()  # Espera o usuário pressionar ENTER
                
                tempo_corrida = random.uniform(2.0, 5.0)
                print(f"🏃‍♂️ Correndo por {tempo_corrida:.1f} segundos...")
                time.sleep(tempo_corrida)
                
                distancia_percorrida = tempo_corrida * distancia_por_segundo
                self.corrida_feita += distancia_percorrida
                self.stamina -= random.randint(8, 15)
                
                if self.stamina < 0:
                    self.stamina = 0
                    
                self.mostrar_progresso()
                
                if self.stamina < 30:
                    print("⚠️  Sua stamina está baixa! Descanse um pouco...")
                    time.sleep(2)
                    self.stamina += 20
                    
        except KeyboardInterrupt:
            print("\n😴 Corrida interrompida...")
            return False
            
        print("\n✅ CORRIDA CONCLUÍDA! Sua resistência aumentou!")
        return True
    
    def iniciar_treino(self):
        print("🚀 INICIANDO TREINO INTENSO!")
        self.typewriter("O Sistema está te observando... Prove seu valor!")
        
        # Flexões
        if not self.minigame_flexoes():
            return False
            
        # Recuperar um pouco de stamina
        self.stamina = min(self.stamina + 30, 100)
        print("\n💧 Beba água e prepare-se para os abdominais!")
        time.sleep(2)
        
        # Abdominais
        if not self.minigame_abdominais():
            return False
            
        # Última recuperação
        self.stamina = min(self.stamina + 20, 100)
        print("\n🌬️  Respire fundo... Hora da corrida!")
        time.sleep(2)
        
        # Corrida
        if not self.minigame_corrida():
            return False
            
        return True
    
    def recompensa_treino(self):
        print("\n" + "⭐" * 60)
        print("⭐ TREINO CONCLUÍDO COM SUCESSO! ⭐")
        print("⭐" * 60)
        
        self.typewriter("\n🎖️  VOCÊ PROVOU SEU VALOR!")
        self.typewriter("💪 Seus músculos estão mais definidos...")
        self.typewriter("🔥 Sua resistência aumentou consideravelmente...")
        self.typewriter("⚡ O Sistema reconhece seu esforço!")
        
        return {
            "forca": random.randint(3, 5),
            "vida": random.randint(2, 4),
            "stamina": random.randint(4, 7)
        }

# COMO USAR NO SEU JOGO:
def cena_treino_sistema():
    print("\nVocê aceita as missões, e agora consegue ver o que precisa ser feito.")
    print("A missão pede para que você faça 100 flexões, 50 abdominais e corra 5km.")
    print("Essa é a única maneira de você se tornar mais forte.")
    
    input("\nPressione ENTER para iniciar o treino...")
    
    minigame = MinigameTreino()
    
    if minigame.iniciar_treino():
        recompensas = minigame.recompensa_treino()
        
        print(f"\n🎯 RECOMPENSAS OBTIDAS:")
        print(f"💪 +{recompensas['forca']} de Força")
        print(f"❤️  +{recompensas['vida']} de Vida") 
        print(f"⚡ +{recompensas['stamina']} de Stamina")
        
        return recompensas
    else:
        print("\n💀 Você falhou no treino... O Sistema está decepcionado.")
        return None