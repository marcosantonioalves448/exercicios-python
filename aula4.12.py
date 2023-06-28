deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))

meses = 1
total_ganho_juros = 0

while meses <= 24:
    montante = deposito_inicial * (1 + taxa_juros / 100) ** meses
    juros = montante - deposito_inicial
    total_ganho_juros += juros

    print(f"Mês {meses}: Valor acumulado = R${montante:.2f} | Juros = R${juros:.2f}")

    meses += 1

print(f"Total ganho com juros no período: R${total_ganho_juros:.2f}")
