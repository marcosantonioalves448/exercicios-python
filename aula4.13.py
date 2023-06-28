divida_inicial = float(input("Digite o valor inicial da dívida: "))
juro_mensal = float(input("Digite a taxa de juros mensal (%): "))
pagamento_mensal = float(input("Digite o valor mensal a ser pago: "))

meses = 0
total_pago = 0
total_juros = 0

while divida_inicial > 0:
    juros = divida_inicial * (juro_mensal / 100)
    divida_inicial += juros
    divida_inicial -= pagamento_mensal

    total_pago += pagamento_mensal
    total_juros += juros
    meses += 1

print(f"Número de meses para pagar a dívida: {meses}")
print(f"Total pago: R${total_pago:.2f}")
print(f"Total de juros pago: R${total_juros:.2f}")
