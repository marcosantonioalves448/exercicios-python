def main():
    pessoa = {}

    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    email = input("Digite o e-mail da pessoa: ")

    pessoa["nome"] = nome
    pessoa["idade"] = idade
    pessoa["email"] = email

    print("\nInformações da pessoa:")
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"E-mail: {pessoa['email']}")

if __name__ == "__main__":
    main()
