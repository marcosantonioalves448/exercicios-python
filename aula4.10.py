ultimo_numero = int(input("Informe o último número: "))

numero_atual = 1

while numero_atual <= ultimo_numero:
    if numero_atual % 2 != 0:
        print(numero_atual)
    numero_atual += 1
