primeiro_numero = float(input('Informe o primeiro número:'))
segundo_numero = float(input('Informe o segundo número:'))
operacao = input('Escolha qual operação fazer, 1 soma, 2 subtração, 3 multiplicação, 4 divisão')

if(operacao == "1"):
    print(primeiro_numero+segundo_numero)
elif operacao == "2":
    print(primeiro_numero-segundo_numero)
elif operacao == "3":
    print(primeiro_numero*segundo_numero)
elif operacao == "4":
    print(primeiro_numero/segundo_numero)
else:
    print('Operação inválida')