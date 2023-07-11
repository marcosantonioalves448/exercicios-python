nomes = []
idades = []
for i in range(5):
    nome = input("Digite o nome da pessoa {}: ")
    idade = int(input("Digite a idade da pessoa {}: "))

    nomes.append(nome)
    idades.append(idade)
print("Nomes:", nomes)
print("Idades:", idades)