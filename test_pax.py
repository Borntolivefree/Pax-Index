from engine import PaxSovereigntyEngine

def run_pax_test():
    pax = PaxSovereigntyEngine()
    
    # Lista de compras simulada
    compras = [
        {"nome": "Fairphone", "id": "fairphone", "socio": "Independente"},
        {"nome": "Telemóvel X", "id": "unknown_tech", "socio": "BlackRock"},
        {"nome": "Pine64", "id": "pine64", "socio": "Comunidade"},
        {"nome": "Lockheed Martin", "id": "lockheed", "socio": "Vanguard"},
        {"nome": "Startup XPTO", "id": "xpto", "socio": "Desconhecido"}
    ]

    print("=== 🍌 RELATÓRIO DE SOBERANIA PAX-INDEX ===\n")

    for item in compras:
        resultado = pax.analyze_source(item["id"], major_shareholder=item["socio"])
        
        print(f"Produto: {item['nome']}")
        print(f"Veredito: {resultado['status']}")
        print(f"Cashback: {resultado['multiplier'] * 80}% (do valor base)")
        print("-" * 40)

if __name__ == "__main__":
    run_pax_test()
