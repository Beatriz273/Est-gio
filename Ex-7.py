faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calcular_percentual(faturamento):
    total_faturamento = sum(faturamento.values())

    percentuais = {}

    for estado, valor in faturamento.items():
        percentual = (valor / total_faturamento) * 100
        percentuais[estado] = percentual

    return percentuais, total_faturamento

def main():
    percentuais, total_faturamento = calcular_percentual(faturamento_por_estado)
    
    print(f"Valor total de faturamento: R${total_faturamento:.2f}")
    print("\nPercentual de representação por estado:")
    
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()