# Pax-Index Engine v1.0 - Sintonia
# Algoritmo de Cálculo de Soberania Ética

def calcular_pax_index(transacao):
    """
    Calcula o índice de impacto de uma transação.
    Retorna uma pontuação de 0 (Aniquilação) a 100 (Soberania).
    """
    score_base = 100
    
    # Critérios de exclusão (Indústria de Guerra/Exploração)
    if transacao['setor'] == 'armamento':
        score_base -= 80
    elif transacao['setor'] == 'extrativismo_conflito':
        score_base -= 50
        
    # Critérios de bonificação (Economia de Vida)
    if transacao['etica'] == True:
        score_base += 20
        
    return min(score_base, 100)

print("Sistema Pax-Index: Motor de Sintonia Ativo.")
