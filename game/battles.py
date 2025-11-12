import random

def luta_inicial(player):
    print("\n" + "╔" + "═" * 58 + "╗")
    print(f"║{'ENCONTRO COM A HORDA DE LOBOS!':^58}║")
    print("╚" + "═" * 58 + "╝")
    
    print("🐺 Inimigo: Horda de Lobos Famintos")
    print(f"❤️  Vida dos Lobos: 20")
    print(f"⚔️  Ataque dos Lobos: 2")
    print("─" * 60)

    vida_lobos = 20
    atq_lobos = 2
    venceu = False

    while vida_lobos > 0 and player.vida > 0 and player.stamina > 0:
        print(f"\n📊 SEU STATUS:")
        print(f"❤️  Sua Vida: {player.vida} | ⚡ Stamina: {player.stamina}")
        print(f"🐺 Vida dos Lobos: {vida_lobos}")
        print("─" * 40)
        
        ataque = input(f"🎯 Qual ataque você deseja usar senhor/a {player.classe}?\n📜 Opções: {', '.join(player.ataques)}\n➡️  ").title()

        if ataque not in player.ataques:
            print("\n❌ Ataque inválido! Você hesitou e os lobos aproveitaram para te atacar!")
            player.vida -= atq_lobos
            continue

        info = player.ataques_info[ataque]
        if player.stamina >= info["stam"]:
            vida_lobos -= info["dano"]
            player.stamina -= info["stam"]
            print(f"\n✨ Você usou '{ataque}'!")
            print(f"💥 Os lobos receberam {info['dano']} de dano. Vida restante: {vida_lobos}. Sua stamina: {player.stamina}")
        else:
            print(f"\n😫 Stamina insuficiente para {ataque}!")
            print("Você perdeu a vez...")
            continue
        
        if vida_lobos <= 0:
            print("\n" + "🎉" * 5)
            print("🎊 Sinceramente... Não achei que você sobreviveria, meus sinceros parabéns. Fracassado.")
            print("🎉" * 5)
            venceu = True
            break
        
        print(f"\n🐺 Agora é a vez dos lobos amigão HAHAHA. Eles te atacam e causam {atq_lobos} de dano.")
        player.vida -= atq_lobos
        print(f"❤️  Sua vida restante: {player.vida}")
        
        if player.vida <= 0:
            print("\n💀" * 5)
            print("☠️  Você morreu! Fracassado!")
            print("💀" * 20)
            break

    if venceu:
        player.descansar()
        player.ganho_nivel()
    else:
        player.descansar()
        print("💤 Pelo menos você pode descansar... fracassado!")

def desafio_inicial(player):
    print("\n" + "─" * 60)
    decisao1 = input("❓ Deseja ir enfrentar um desafio onde você provavelmente irá morrer, mas se sair vivo irá aumentar muito seus atributos por agora? (S/N)\n➡️  ").upper()

    while decisao1 not in ("S", "N"):
        decisao1 = input("❌ Resposta inválida. Por favor, responda com 'S' para sim ou 'N' para não: ").upper()

    if decisao1 == "S":
        print("\n🔥 CORAJOSO! Avistamos uma dungeon e entramos nela...")
        luta_inicial(player)
    else:
        print(f"\n🐔 Você decidiu não enfrentar o desafio por agora. É a primeira vez que vejo um {player.classe} medroso!\nBoa sorte ao encarar os desafios daqui para frente sem ter upado nada.")

    
def batalha_goblins(player):
    print("\n" + "╔" + "═" * 58 + "╗")
    print(f"║{'BATALHA CONTRA OS GOBLINS GUARDIÕES!':^58}║")
    print("╚" + "═" * 58 + "╝")
    
    print("👹 Inimigo: Goblin Guardião + 2 Goblin Peões")
    print(f"❤️  Vida do Goblin Guardião: 15")
    print(f"❤️  Vida dos Goblin Peões: 5 cada")
    print(f"⚔️  Ataque do Guardião: 3 | Ataque dos Peões: 1")
    print("💬 'GRRR! Ninguém passa!'")
    print("─" * 60)

    vida_guardiao = 15
    vida_peao1 = 5
    vida_peao2 = 5
    venceu = False
    turno = 1

    while (vida_guardiao > 0 or vida_peao1 > 0 or vida_peao2 > 0) and player.vida > 0 and player.stamina > 0:
        print(f"\n🎯 TURNO {turno}")
        print(f"📊 SEU STATUS: ❤️ {player.vida} | ⚡ {player.stamina}")
        print(f"👹 INIMIGOS: Guardião ❤️{vida_guardiao} | Peão1 ❤️{vida_peao1} | Peão2 ❤️{vida_peao2}")
        print("─" * 50)
        
        # MOSTRAR ATAQUES ESPECIAIS CONTRA GOBLINS
        print("🎯 ESCOLHA SEU ALVO:")
        alvos = []
        if vida_guardiao > 0:
            alvos.append("Guardião")
            print("🔴 1- Goblin Guardião (Vida: 15, Ataque: 3) - LÍDER")
        if vida_peao1 > 0:
            alvos.append("Peão1")
            print("🟡 2- Goblin Peão 1 (Vida: 5, Ataque: 1) - FRACO")
        if vida_peao2 > 0:
            alvos.append("Peão2") 
            print("🟢 3- Goblin Peão 2 (Vida: 5, Ataque: 1) - FRACO")
        
        escolha = input("\n🎯 Escolha o alvo (1/2/3) ou digite o nome do ataque: ")

        # SISTEMA DE ALVO + ATAQUE
        if escolha in ["1", "2", "3"]:
            alvo_escolhido = alvos[int(escolha)-1] if escolha.isdigit() and 1 <= int(escolha) <= len(alvos) else None
            if alvo_escolhido:
                ataque = input(f"🎯 Qual ataque usar em {alvo_escolhido}? {', '.join(player.ataques)}: ").title()
            else:
                print("❌ Alvo inválido! Você fica confuso...")
                player.vida -= 2
                continue
        else:
            ataque = escolha.title()
            alvo_escolhido = "Guardião"  # Alvo padrão se não especificar

        if ataque not in player.ataques:
            print("❌ Ataque inválido! Os goblins riem da sua incompetência!")
            player.vida -= 2
            continue

        info = player.ataques_info[ataque]
        if player.stamina >= info["stam"]:
            player.stamina -= info["stam"]
            dano = info["dano"]
            
            # APLICAR DANO NO ALVO ESCOLHIDO
            if alvo_escolhido == "Guardião" and vida_guardiao > 0:
                vida_guardiao -= dano
                print(f"\n✨ Você usou '{ataque}' no Goblin Guardião!")
                print(f"💥 Causou {dano} de dano! ❤️ Guardião: {max(0, vida_guardiao)}")
            elif alvo_escolhido == "Peão1" and vida_peao1 > 0:
                vida_peao1 -= dano
                print(f"\n✨ Você usou '{ataque}' no Goblin Peão 1!")
                print(f"💥 Causou {dano} de dano! ❤️ Peão 1: {max(0, vida_peao1)}")
            elif alvo_escolhido == "Peão2" and vida_peao2 > 0:
                vida_peao2 -= dano
                print(f"\n✨ Você usou '{ataque}' no Goblin Peão 2!")
                print(f"💥 Causou {dano} de dano! ❤️ Peão 2: {max(0, vida_peao2)}")
            else:
                print("🎯 Alvo já está derrotado! Ataque desperdiçado...")
        else:
            print(f"😫 Stamina insuficiente para {ataque}!")
            print("Você tropeça e fica vulnerável!")
            continue
        
        # VERIFICAR VITÓRIA
        if vida_guardiao <= 0 and vida_peao1 <= 0 and vida_peao2 <= 0:
            print("\n" + "🎉" * 8)
            print("🏆 VITÓRIA! Você derrotou todos os goblins!")
            print("🚪 A entrada da dungeon está livre!")
            print("💀 Mas não se ache especial... ainda é um fracassado!")
            print("🎉" * 8)
            venceu = True
            break
        
        # ATAQUE DOS GOBLINS (MAIS ESTRATÉGICO)
        print(f"\n👹 VEZ DOS GOBLINS!")
        dano_total_goblins = 0
        
        if vida_guardiao > 0:
            player.vida -= 3
            dano_total_goblins += 3
            print("🔴 Goblin Guardião te ataca com seu machado! (-3❤️)")
        
        if vida_peao1 > 0:
            player.vida -= 1
            dano_total_goblins += 1
            print("🟡 Goblin Peão 1 te joga uma pedra! (-1❤️)")
            
        if vida_peao2 > 0:
            player.vida -= 1  
            dano_total_goblins += 1
            print("🟢 Goblin Peão 2 te ataca com uma faca! (-1❤️)")
        
        print(f"💔 Dano total recebido: {dano_total_goblins}")
        print(f"❤️  Sua vida restante: {player.vida}")
        
        # FRASES ALEATÓRIAS DOS GOBLINS
        frases_goblins = [
            "'Morra, intruso!'",
            "'Ninguém passa por nós!'", 
            "'Sua carne vai virar jantar!'",
            "'Hihihi, ele está sangrando!'"
        ]
        print(f"💬 Goblins: {random.choice(frases_goblins)}")
        
        if player.vida <= 0:
            print("\n💀" * 8)
            print("☠️  VOCÊ FOI DERROTADO PELOS GOBLINS!")
            print("💀 Os goblins festejam com seus pertences...")
            print("💀" * 8)
            break
            
        turno += 1

    if venceu:
        player.descansar()
        player.ganho_nivel()
        print("\n🔮 Agora você pode entrar na dungeon...")
        print("📖 O que segredos ela guarda?")
    else:
        player.descansar()
        print("\n💤 Você recua enquanto os goblins zombam...")
        print("🐔 Talvez seja melhor treinar mais, fracassado!")