class SovereigntyScorer:
    def __init__(self):
        # Pesos de risco para a soberania do utilizador
        self.risk_factors = {
            "excessive_telemetry": 0.4,
            "biometric_capture": 0.3,
            "unauthorized_sync": 0.2,
            "forced_cloud_dependency": 0.1
        }

    def calculate_impact(self, system_logs):
        """
        Analisa logs do sistema para determinar o nível de invasão.
        """
        impact_score = 0
        found_risks = []

        for risk, weight in self.risk_factors.items():
            if system_logs.get(risk):
                impact_score += weight * 100
                found_risks.append(risk)

        # O índice de Sintonia é o inverso do impacto de risco
        sintonia_index = max(0, 100 - impact_score)
        return sintonia_index, found_risks

# Exemplo de uso
if __name__ == "__main__":
    # Simulação de um log de sistema invasivo
    current_logs = {
        "excessive_telemetry": True,
        "forced_cloud_dependency": True,
        "biometric_capture": False
    }

    scorer = SovereigntyScorer()
    score, risks = scorer.calculate_impact(current_logs)

    print(f"🛡️ Índice de Sintonia: {score}/100")
    print(f"⚠️ Riscos detetados: {', '.join(risks)}")
