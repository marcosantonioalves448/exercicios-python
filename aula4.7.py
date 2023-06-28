usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "jardim":
    if senha == "flores1206":
        print("Seja bem-vindo!")
    else:
        print("Usuário e senha não conferem.")
elif usuario == "cordeiro":
    if senha == "la1506":
        print("Seja bem-vindo!")
    else:
        print("Usuário e senha não conferem.")
else:
    print("Usuário e senha não conferem.")
