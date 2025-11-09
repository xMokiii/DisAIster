# import asyncio
# from deathByai import DeathByAI

# async def test_game():
#     """Test simple du jeu Death by AI"""
    
#     # Créer le jeu
#     game = DeathByAI()
    
#     print("=== DEATH BY AI - TEST ===\n")
    
#     try:
#         # 1. Générer un scénario
#         print("🎲 Génération du scénario...")
#         scenario = await game.generate_scenario()
#         print(f"📖 Scénario: {scenario}\n")
        
#         # 2. Demander l'action du joueur
#         player_action = input("💭 Comment survivez-vous? : ")
#         print()
        
#         # 3. Évaluer la survie
#         print("🤖 L'IA réfléchit...")
#         result = await game.evaluate_survival(player_action)
        
#         # 4. Afficher le résultat
#         if result["survived"]:
#             print("🎉 VOUS SURVIVEZ! 🎉")
#         else:
#             print("💀 VOUS ÊTES MORT! 💀")
        
#         print(f"📝 {result['explanation']}")
        
#     except Exception as e:
#         print(f"❌ Erreur: {e}")
#         print("Vérifiez qu'Ollama est lancé et que le modèle llama3.2 est installé")

# if __name__ == "__main__":
#     asyncio.run(test_game())