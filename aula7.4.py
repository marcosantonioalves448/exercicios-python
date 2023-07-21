def main():
    produtos = {}

    for i in range(3):
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))

        produtos[nome_produto] = preco_produto

    print("\nProdutos e preços inseridos:")
    for produto, preco in produtos.items():
        print(f"{produto}: R${preco:.2f}")

if __name__ == "__main__":
    main()
