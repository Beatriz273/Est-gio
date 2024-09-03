faturamento = {
    "faturamento": [
        {"dia": 1, "valor": 1200},
        {"dia": 2, "valor": 1500},
        {"dia": 3, "valor": 800},
        {"dia": 4, "valor": 0},
        {"dia": 5, "valor": 1700},
        {"dia": 6, "valor": 0},
        {"dia": 7, "valor": 1000},
        {"dia": 8, "valor": 0},
        {"dia": 9, "valor": 2000},
        {"dia": 10, "valor": 0},
        {"dia": 11, "valor": 1400}
    ]
}

def analisar_faturamento(dados):
    valores = [item['valor'] for item in dados if item['valor'] > 0]

    if not valores:
        return None, None, 0

    menor_valor = min(valores)
    maior_valor = max(valores)
    
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for item in dados if item['valor'] > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_media

def main():
    dados = faturamento['faturamento']
    
    menor_valor, maior_valor, dias_acima_media = analisar_faturamento(dados)
    
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()