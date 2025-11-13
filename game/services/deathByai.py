from ollama import AsyncClient
import random
import time

class DeathByAI:
    def __init__(self, model="gemma3:4b", max_chars=500, host='http://localhost:11434'):
        self.model = model
        self.max_chars = max_chars
        self.host = host
        self.current_scenario = None
        self.used_scenarios = set()

        self.prompt = """
Génère UN scénario de survie RÉALISTE et DANGEREUX en français. Format: "Vous êtes [situation]"

EXEMPLES ACCEPTABLES:
- Vous êtes pris dans une avalanche de neige qui dévale vers vous.
- Vous êtes face à un ours grizzly affamé dans une forêt.
- Vous êtes dans un ascenseur en chute libre.
- Vous êtes cerné par un incendie de forêt.
- Vous êtes dans une voiture qui fonce vers un précipice sans freins.

THÈMES AUTORISÉS UNIQUEMENT:
- Catastrophes naturelles (tornades, séismes, inondations, avalanches)
- Animaux dangereux réels (ours, requins, serpents, loups)
- Accidents mécaniques (ascenseurs, voitures, avions, trains)
- Situations urbaines dangereuses (incendies, effondrements, explosions)
- Conditions météo extrêmes (blizzard, tempête, canicule mortelle)

INTERDICTIONS STRICTES:
- Pas d'objets magiques ou fantastiques
- Pas d'objets inoffensifs rendus dangereux (pétales, nuages roses, etc.)
- Pas de créatures imaginaires
- Pas de situations impossibles physiquement
- Exception en cas d'humour absurde ou de références pop culture ridicules

RÈGLES:
- Commencer par "Vous êtes"
- Danger immédiat et RÉALISTE
- Une seule phrase claire, pas trop de détails, 12 mots max
- Scenario crédible qui pourrait arriver dans la vraie vie

Génère UN scénario RÉALISTE maintenant."""
        
    async def generate_scenario(self):
        """Génère un scénario de survie mortel"""
        client = AsyncClient(self.host)
        response = await client.chat(model=self.model,messages=[{
                "role": "system", 
                "content": self.prompt 
            }]
        )
        self.current_scenario = response['message']['content'][:self.max_chars]
        return self.current_scenario
    
    async def evaluate_survival(self, player_action):
        """Évalue si le joueur survit"""
        client = AsyncClient(host=self.host)
        prompt = f"""
        Scénario: {self.current_scenario}
        Action du joueur: {player_action}
        
        Réponds en français en MAXIMUM 3 phrases:
        RÉSULTAT: SURVIT ou MEURT
        RAISON: [explication courte et dramatique]
        """
        
        response = await client.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        result = response['message']['content'][:self.max_chars]
        survived = "SURVIT" in result.upper()
        
        return {
            "survived": survived,
            "explanation": result
        }
    
    def reset_game(self): 
        "Nouvelle partie"
        self.current_scenario = None
