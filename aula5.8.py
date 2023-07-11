numeros = []
while True:
    numero = float(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

if numeros:
    quantidade_numeros = len(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)

    print("Quantidade de números digitados:", quantidade_numeros)
    print("Valor máximo:", valor_maximo)
    print("Valor mínimo:", valor_minimo)
else:
    print("Nenhum número foi digitado (exceto 0).")