senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Olá! Seja bem-vindo ao banco!")
        break

    tentativas -= 1
    if tentativas > 0:
        print("Senha incorreta! Você ainda tem", tentativas, "tentativas.")
    else:
        print("Sua senha foi bloqueada! Por favor, dirija-se à agência.")
