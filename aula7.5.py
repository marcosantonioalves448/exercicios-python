def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    vogais_contagem = {}

    for letra in texto:
        if letra in vogais:
            vogais_contagem[letra] = vogais_contagem.get(letra, 0) + 1

    return vogais_contagem

def main():
    texto = input("Digite o texto: ")
    resultado = contar_vogais(texto)

    print("\nQuantidade de vogais no texto:")
    for vogal, quantidade in resultado.items():
        print(f"{vogal}: {quantidade}")

if __name__ == "__main__":
    main()
