N = int(input("Digite um número inteiro: "))
if N % 2 == 0:
    output = list(range(N, -N - 1, -2))
else:
    output = list(range(N - 1, -N - 1, -2))

for numero in output:
    print(numero)