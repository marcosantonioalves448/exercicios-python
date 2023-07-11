numero = int(input("Digite um número inteiro: "))

divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
print("Quantidade de divisores:", len(divisores))
print("Divisores:", divisores)