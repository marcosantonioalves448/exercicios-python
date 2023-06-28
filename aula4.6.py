distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 300:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print("O preço da passagem é R$", preco)
