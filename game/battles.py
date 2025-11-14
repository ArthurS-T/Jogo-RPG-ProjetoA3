import random
import time
import sys

def typewriter(text, delay=0.06):
    """Efeito máquina de escrever estilo Undertale"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dramatic_print(text, delay=0.08):
    """Print dramático com pausas naturais"""
    words = text.split()
    for i, word in enumerate(words):
        print(word, end=' ', flush=True)
        time.sleep(delay)
        # Pausa natural no final de frases
        if word.endswith(('.', '!', '?', '...')):
            time.sleep(delay * 3)
    print()

def input_typewriter(prompt, delay=0.06):
    """Input com efeito typewriter"""
    typewriter(prompt, delay)
    return input("➡️  ")

def game_over():
    """Finaliza o jogo quando o player morre"""
    dramatic_print("\n" + "💀" * 20)
    dramatic_print("🎮 FIM DE JOGO - VOCÊ MORREU")
    dramatic_print("💀" * 20)
    dramatic_print("\nO sistema está finalizando...")
    time.sleep(2)
    sys.exit()

def luta_inicial(player):
    print("\n" + "╔" + "═" * 58 + "╗")
    dramatic_print(f"║{'ENCONTRO COM A HORDA DE LOBOS!':^58}║")
    print("╚" + "═" * 58 + "╝")
    
    dramatic_print("🐺 Inimigo: Horda de Lobos Famintos")
    dramatic_print(f"❤️  Vida dos Lobos: 20")
    dramatic_print(f"⚔️  Ataque dos Lobos: 2")
    dramatic_print("─" * 60)

    vida_lobos = 20
    atq_lobos = 2
    venceu = False

    while vida_lobos > 0 and player.vida > 0 and player.stamina > 0:
        dramatic_print(f"\n📊 SEU STATUS:")
        dramatic_print(f"❤️  Sua Vida: {player.vida} | ⚡ Stamina: {player.stamina}")
        dramatic_print(f"🐺 Vida dos Lobos: {vida_lobos}")
        dramatic_print("─" * 40)
        
        ataque = input_typewriter(f"🎯 Qual ataque você deseja usar senhor/a {player.classe}?\n📜 Opções: {', '.join(player.ataques)}\n").title()

        if ataque not in player.ataques:
            dramatic_print("\n❌ Ataque inválido! Você hesitou e os lobos aproveitaram para te atacar!")
            player.vida -= atq_lobos
            dramatic_print(f"🐺 Os lobos te atacam e causam {atq_lobos} de dano.")
            dramatic_print(f"❤️  Sua vida restante: {player.vida}")
            
            if player.vida <= 0:
                dramatic_print("\n💀" * 5)
                dramatic_print("☠️  Desde o inicio eu já sabia o quão fracassado você era, só não sabia que era tanto, você morreu")
                dramatic_print("💀" * 20)
                game_over()
            continue

        info = player.ataques_info[ataque]
        if player.stamina >= info["stam"]:
            vida_lobos -= info["dano"]
            player.stamina -= info["stam"]
            dramatic_print(f"\n✨ Você usou '{ataque}'!")
            dramatic_print(f"💥 Os lobos receberam {info['dano']} de dano. Vida restante: {vida_lobos}. Sua stamina: {player.stamina}")
        else:
            dramatic_print(f"\n😫 Stamina insuficiente para {ataque}!")
            dramatic_print("Você perdeu a vez e os lobos te atacam!")
            player.vida -= atq_lobos
            dramatic_print(f"🐺 Os lobos te atacam e causam {atq_lobos} de dano.")
            dramatic_print(f"❤️  Sua vida restante: {player.vida}")
            
            if player.vida <= 0:
                dramatic_print("\n💀" * 5)
                dramatic_print("☠️  Desde o inicio eu já sabia o quão fracassado você era, só não sabia que era tanto, você morreu")
                dramatic_print("💀" * 20)
                game_over()
            continue
        
        if vida_lobos <= 0:
            dramatic_print("\n" + "🎉" * 5)
            dramatic_print("🎊 Sinceramente... Não achei que você sobreviveria, meus sinceros parabéns. Fracassado.")
            dramatic_print("🎉" * 5)
            venceu = True
            break
        
        dramatic_print(f"\n🐺 Agora é a vez dos lobos amigão HAHAHA. Eles te atacam e causam {atq_lobos} de dano.")
        player.vida -= atq_lobos
        dramatic_print(f"❤️  Sua vida restante: {player.vida}")
        
        if player.vida <= 0:
            dramatic_print("\n💀" * 5)
            dramatic_print("☠️  Desde o inicio eu já sabia o quão fracassado você era, só não sabia que era tanto, você morreu")
            dramatic_print("💀" * 20)
            game_over()

    if venceu:
        player.descansar()
        player.ganho_nivel()
        return True
    else:
        player.descansar()
        dramatic_print("💤 Pelo menos você pode descansar... fracassado!")
        return False

def desafio_inicial(player):
    dramatic_print("\n" + "─" * 60)
    decisao1 = input_typewriter("❓ Deseja ir enfrentar um desafio onde você provavelmente irá morrer, mas se sair vivo irá aumentar muito seus atributos por agora? (S/N)\n").upper()

    while decisao1 not in ("S", "N"):
        decisao1 = input_typewriter("❌ Resposta inválida. Por favor, responda com 'S' para sim ou 'N' para não: ").upper()

    if decisao1 == "S":
        dramatic_print("\n🔥 CORAJOSO! Avistamos uma dungeon e entramos nela...")
        return luta_inicial(player)
    else:
        dramatic_print(f"\n🐔 Você decidiu não enfrentar o desafio por agora. É a primeira vez que vejo um {player.classe} medroso!")
        dramatic_print("Boa sorte ao encarar os desafios daqui para frente sem ter upado nada.")
        return True

def batalha_goblins(player):
    print("\n" + "╔" + "═" * 58 + "╗")
    dramatic_print(f"║{'BATALHA CONTRA OS GOBLINS GUARDIÕES!':^58}║")
    print("╚" + "═" * 58 + "╝")
    
    dramatic_print("👹 Inimigo: Goblin Guardião + 2 Goblin Peões")
    dramatic_print(f"❤️  Vida do Goblin Guardião: 15")
    dramatic_print(f"❤️  Vida dos Goblin Peões: 5 cada")
    dramatic_print(f"⚔️  Ataque do Guardião: 3 | Ataque dos Peões: 1")
    dramatic_print("💬 'GRRR! Ninguém passa!'")
    dramatic_print("─" * 60)

    vida_guardiao = 15
    vida_peao1 = 5
    vida_peao2 = 5
    venceu = False
    turno = 1

    while (vida_guardiao > 0 or vida_peao1 > 0 or vida_peao2 > 0) and player.vida > 0 and player.stamina > 0:
        dramatic_print(f"\n🎯 TURNO {turno}")
        dramatic_print(f"📊 SEU STATUS: ❤️ {player.vida} | ⚡ {player.stamina}")
        dramatic_print(f"👹 INIMIGOS: Guardião ❤️{max(0, vida_guardiao)} | Peão1 ❤️{max(0, vida_peao1)} | Peão2 ❤️{max(0, vida_peao2)}")
        dramatic_print("─" * 50)
        
        # SISTEMA DE ALVO CORRIGIDO
        alvos_disponiveis = []
        dramatic_print("🎯 ESCOLHA SEU ALVO:")
        
        if vida_guardiao > 0:
            alvos_disponiveis.append("Guardião")
            dramatic_print("🔴 1- Goblin Guardião (Vida: 15, Ataque: 3) - LÍDER")
        if vida_peao1 > 0:
            alvos_disponiveis.append("Peão1")
            dramatic_print("🟡 2- Goblin Peão 1 (Vida: 5, Ataque: 1) - FRACO")
        if vida_peao2 > 0:
            alvos_disponiveis.append("Peão2") 
            dramatic_print("🟢 3- Goblin Peão 2 (Vida: 5, Ataque: 1) - FRACO")
        
        escolha = input_typewriter("\n🎯 Escolha o alvo (1/2/3) ou digite o nome do ataque: ")

        # CORREÇÃO DO SISTEMA DE ALVO
        alvo_escolhido = None
        ataque = None
        
        if escolha in ["1", "2", "3"]:
            escolha_num = int(escolha)
            if 1 <= escolha_num <= len(alvos_disponiveis):
                alvo_escolhido = alvos_disponiveis[escolha_num-1]
                ataque = input_typewriter(f"🎯 Qual ataque usar em {alvo_escolhido}? {', '.join(player.ataques)}: ").title()
            else:
                dramatic_print("❌ Alvo inválido! Você fica confuso e os goblins te atacam!")
                # ATAQUE DOS GOBLINS POR ERRO DE ALVO
                dano_total_goblins = 0
                if vida_guardiao > 0:
                    player.vida -= 3
                    dano_total_goblins += 3
                    dramatic_print("🔴 Goblin Guardião te ataca com seu machado! (-3❤️)")
                if vida_peao1 > 0:
                    player.vida -= 1
                    dano_total_goblins += 1
                    dramatic_print("🟡 Goblin Peão 1 te joga uma pedra! (-1❤️)")
                if vida_peao2 > 0:
                    player.vida -= 1  
                    dano_total_goblins += 1
                    dramatic_print("🟢 Goblin Peão 2 te ataca com uma faca! (-1❤️)")
                
                dramatic_print(f"💔 Dano total recebido: {dano_total_goblins}")
                dramatic_print(f"❤️  Sua vida restante: {player.vida}")
                
                if player.vida <= 0:
                    dramatic_print("\n💀" * 8)
                    dramatic_print("☠️  Desde o inicio eu já sabia o quão fracassado você era, só não sabia que era tanto, você morreu")
                    dramatic_print("💀" * 8)
                    game_over()
                continue
        else:
            ataque = escolha.title()
            # ESCOLHER ALVO AUTOMATICAMENTE SE NÃO ESPECIFICADO
            if vida_peao1 > 0:
                alvo_escolhido = "Peão1"
            elif vida_peao2 > 0:
                alvo_escolhido = "Peão2" 
            elif vida_guardiao > 0:
                alvo_escolhido = "Guardião"
            else:
                dramatic_print("❌ Nenhum alvo disponível!")
                continue

        # VERIFICAÇÃO DE ATAQUE INVÁLIDO
        if ataque not in player.ataques:
            dramatic_print("❌ Ataque inválido! Os goblins riem da sua incompetência e te atacam!")
            # ATAQUE DOS GOBLINS POR ATAQUE INVÁLIDO
            dano_total_goblins = 0
            if vida_guardiao > 0:
                player.vida -= 3
                dano_total_goblins += 3
                dramatic_print("🔴 Goblin Guardião te ataca com seu machado! (-3❤️)")
            if vida_peao1 > 0:
                player.vida -= 1
                dano_total_goblins += 1
                dramatic_print("🟡 Goblin Peão 1 te joga uma pedra! (-1❤️)")
            if vida_peao2 > 0:
                player.vida -= 1  
                dano_total_goblins += 1
                dramatic_print("🟢 Goblin Peão 2 te ataca com uma faca! (-1❤️)")
            
            dramatic_print(f"💔 Dano total recebido: {dano_total_goblins}")
            dramatic_print(f"❤️  Sua vida restante: {player.vida}")
            
            if player.vida <= 0:
                dramatic_print("\n💀" * 8)
                dramatic_print("☠️  Desde o inicio eu já sabia o quão fracassado você era, só não sabia que era tanto, você morreu")
                dramatic_print("💀" * 8)
                game_over()
            continue

        info = player.ataques_info[ataque]
        
        # VERIFICAÇÃO DE STAMINA INSUFICIENTE
        if player.stamina < info["stam"]:
            dramatic_print(f"😫 Stamina insuficiente para {ataque}!")
            dramatic_print("Você tropeça e fica vulnerável! Os goblins te atacam!")
            # ATAQUE DOS GOBLINS POR STAMINA INSUFICIENTE
            dano_total_goblins = 0
            if vida_guardiao > 0:
                player.vida -= 3
                dano_total_goblins += 3
                dramatic_print("🔴 Goblin Guardião te ataca com seu machado! (-3❤️)")
            if vida_peao1 > 0:
                player.vida -= 1
                dano_total_goblins += 1
                dramatic_print("🟡 Goblin Peão 1 te joga uma pedra! (-1❤️)")
            if vida_peao2 > 0:
                player.vida -= 1  
                dano_total_goblins += 1
                dramatic_print("🟢 Goblin Peão 2 te ataca com uma faca! (-1❤️)")
            
            dramatic_print(f"💔 Dano total recebido: {dano_total_goblins}")
            dramatic_print(f"❤️  Sua vida restante: {player.vida}")
            
            if player.vida <= 0:
                dramatic_print("\n💀" * 8)
                dramatic_print("☠️  Desde o inicio eu já sabia o quão fracassado você era, só não sabia que era tanto, você morreu")
                dramatic_print("💀" * 8)
                game_over()
            continue

        # ATAQUE BEM-SUCEDIDO
        player.stamina -= info["stam"]
        dano = info["dano"]
        
        # APLICAR DANO CORRETAMENTE
        if alvo_escolhido == "Guardião" and vida_guardiao > 0:
            vida_guardiao -= dano
            dramatic_print(f"\n✨ Você usou '{ataque}' no Goblin Guardião!")
            dramatic_print(f"💥 Causou {dano} de dano! ❤️ Guardião: {max(0, vida_guardiao)}")
        elif alvo_escolhido == "Peão1" and vida_peao1 > 0:
            vida_peao1 -= dano
            dramatic_print(f"\n✨ Você usou '{ataque}' no Goblin Peão 1!")
            dramatic_print(f"💥 Causou {dano} de dano! ❤️ Peão 1: {max(0, vida_peao1)}")
        elif alvo_escolhido == "Peão2" and vida_peao2 > 0:
            vida_peao2 -= dano
            dramatic_print(f"\n✨ Você usou '{ataque}' no Goblin Peão 2!")
            dramatic_print(f"💥 Causou {dano} de dano! ❤️ Peão 2: {max(0, vida_peao2)}")
        else:
            dramatic_print("🎯 Alvo já está derrotado! Ataque desperdiçado...")
        
        # VERIFICAR VITÓRIA
        if vida_guardiao <= 0 and vida_peao1 <= 0 and vida_peao2 <= 0:
            dramatic_print("\n" + "🎉" * 8)
            dramatic_print("🏆 VITÓRIA! Você derrotou todos os goblins!")
            dramatic_print("🚪 A entrada da dungeon está livre!")
            dramatic_print("⭐ Bom trabalho, aventureiro!")
            dramatic_print("🎉" * 8)
            venceu = True
            break
        
        # ATAQUE DOS GOBLINS (TURNO NORMAL)
        dramatic_print(f"\n👹 VEZ DOS GOBLINS!")
        dano_total_goblins = 0
        
        if vida_guardiao > 0:
            player.vida -= 3
            dano_total_goblins += 3
            dramatic_print("🔴 Goblin Guardião te ataca com seu machado! (-3❤️)")
        
        if vida_peao1 > 0:
            player.vida -= 1
            dano_total_goblins += 1
            dramatic_print("🟡 Goblin Peão 1 te joga uma pedra! (-1❤️)")
            
        if vida_peao2 > 0:
            player.vida -= 1  
            dano_total_goblins += 1
            dramatic_print("🟢 Goblin Peão 2 te ataca com uma faca! (-1❤️)")
        
        dramatic_print(f"💔 Dano total recebido: {dano_total_goblins}")
        dramatic_print(f"❤️  Sua vida restante: {player.vida}")
        
        frases_goblins = [
            "'Morra, intruso!'",
            "'Ninguém passa por nós!'", 
            "'Sua carne vai virar jantar!'",
            "'Hihihi, ele está sangrando!'"
        ]
        dramatic_print(f"💬 Goblins: {random.choice(frases_goblins)}")
        
        if player.vida <= 0:
            dramatic_print("\n💀" * 8)
            dramatic_print("☠️  Desde o inicio eu já sabia o quão fracassado você era, só não sabia que era tanto, você morreu")
            dramatic_print("💀" * 8)
            game_over()
            
        turno += 1

    if venceu:
        player.descansar()
        player.ganho_nivel()
        dramatic_print("\n🔮 Agora você pode entrar na dungeon...")
        return True
    else:
        player.descansar()
        dramatic_print("\n💤 Você recua enquanto os goblins zombam...")
        dramatic_print("💪 Você não é forte o suficiente, não passa de um fracassado. Vá treinar mais, fracote!")
        return False