class PaxSovereigntyEngine:
    def __init__(self):
        # 1. Base de Dados de Entidades Auditadas
        self.registry = {
            "lockheed": {"name": "Lockheed Martin", "class": "RED", "reason": "Fabricante direto de armamento."},
            "blackrock": {"name": "BlackRock", "class": "RED", "reason": "Financiamento maioritário da indústria bélica."},
            "fronteira_tech": {"name": "SafeBorder S.A.", "class": "YELLOW", "reason": "Defesa civil e segurança de infraestruturas."},
            "fairphone": {"name": "Fairphone", "class": "GREEN", "reason": "Soberania civil e materiais éticos."},
            "pine64": {"name": "Pine64", "class": "GREEN", "reason": "Hardware aberto e focado na privacidade."}
        }

        # 2. Lista de "Contaminação" Financeira
        self.war_shareholders = ["BlackRock", "Vanguard", "State Street"]

    def analyze_source(self, provider_name, major_shareholder=None):
        provider = provider_name.lower()
        
        # A. Verificação de Acionista (Rastreio de Capital Indireto)
        if major_shareholder in self.war_shareholders:
            return {
                "class": "RED",
                "status": f"🔴 RED (Indireto): {provider_name} é detida por {major_shareholder} (Financiador de conflitos).",
                "multiplier": 0.0
            }

        # B. Verificação no Registo Auditado
        data = self.registry.get(provider)
        
        # C. Caso a empresa não esteja na base de dados (A Proteção contra Calúnia)
        if not data:
            return {
                "class": "GREY",
                "status": f"⚪ GREY: {provider_name} ainda não foi auditada. Cashback suspenso por falta de dados.",
                "multiplier": 0.0,
                "action": "Solicitar Auditoria de Transparência"
            }

        # D. Definição de Multiplicadores
        multipliers = {"RED": 0.0, "YELLOW": 0.5, "GREEN": 1.0}
        icon = "🟢" if data["class"] == "GREEN" else "🟡" if data["class"] == "YELLOW" else "🔴"
        
        return {
            "class": data["class"],
            "status": f"{icon} {data['class']}: {data['name']} - {data['reason']}",
            "multiplier": multipliers[data["class"]]
        }

# --- TESTE DO MOTOR ---
if __name__ == "__main__":
    pax = PaxSovereigntyEngine()
    
    # Teste de empresa desconhecida (Não é calúnia, é falta de auditoria)
    print(pax.analyze_source("Empresa_Nova_X")["status"])
    
    # Teste de empresa Green
    print(pax.analyze_source("pine64")["status"])
