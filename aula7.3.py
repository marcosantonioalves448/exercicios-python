def main():
    D = {'pares': [], 'impares': []}

    for _ in range(10):
        numero = int(input("Digite um número inteiro: "))

        if numero % 2 == 0:
            D['pares'].append(numero)
        else:
            D['impares'].append(numero)

    print("\nNúmeros pares:", D['pares'])
    print("Números ímpares:", D['impares'])

if __name__ == "__main__":
    main()
