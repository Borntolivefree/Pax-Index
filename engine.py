class PaxSovereigntyEngine:
    def __init__(self):
        # Base de Dados Ética: Empresas e seus vínculos de capital
        self.registry = {
            "lockheed": {
                "name": "Lockheed Martin",
                "class": "RED",
                "reason": "Complexo Industrial-Militar: Armamento Ofensivo.",
                "alt": "Projetos Aeroespaciais Civis"
            },
            "palantir": {
                "name": "Palantir Technologies",
                "class": "YELLOW",
                "reason": "Defesa de Fronteiras e Inteligência Civil.",
                "alt": "Protocolos de Dados Open Source"
            },
            "fairphone": {
                "name": "Fairphone",
                "class": "GREEN",
                "reason": "Soberania do Utilizador e Cadeia de Valor Ética.",
                "alt": None
            }
        }

    def evaluate_transaction(self, entity_id):
        """
        Avalia o destino do capital e define o multiplicador de Cashback.
        RED: 0% | YELLOW: 40% | GREEN: 80%
        """
        entity = entity_id.lower()
        data = self.registry.get(entity, {"class": "RED", "reason": "Entidade Desconhecida/Sem Auditoria Ética.", "alt": "Alternativas Independentes"})

        classification = data["class"]
        
        if classification == "RED":
            multiplier = 0.0
            status_msg = f"🔴 BLOQUEADO: O capital para {data['name']} financia agressão bélica."
        elif classification == "YELLOW":
            multiplier = 0.5 # 50% do Cashback base (40% total)
            status_msg = f"🟡 AVISO: {data['name']} atua em Defesa Civil/Fronteiras. Uso limitado."
        else:
            multiplier = 1.0 # 100% do Cashback base (80% total)
            status_msg = f"🟢 GREEN: {data['name']} é compatível com a Soberania e a Paz."

        return {
            "status": status_msg,
            "multiplier": multiplier,
            "suggestion": data.get("alt")
        }

# Simulação de interface da DApp
if __name__ == "__main__":
    pax = PaxSovereigntyEngine()
    
    # Teste de um cenário de compra
    result = pax.evaluate_transaction("lockheed")
    print(result["status"])
    print(f"Sugestão de Desvio: {result['suggestion']}")
    print(f"Multiplicador de Recompensa: {result['multiplier'] * 100}%")

