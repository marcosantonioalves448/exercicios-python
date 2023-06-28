# Solicitar salário e cargo
salario = float(input("Digite o salário do funcionário: "))
cargo = input("Digite o cargo do funcionário: ")

# Calcular novo salário
if cargo == "Gerente Geral" or cargo == "Gerente de Relacionamento":
    novo_salario = salario * 1.3
elif cargo == "Analista":
    novo_salario = salario * 1.25
elif cargo == "Assistente de Atendimento":
    novo_salario = salario * 1.2
else:
    print("Cargo inválido")
    novo_salario = None

# Imprimir novo salário, se não for cargo inválido
if novo_salario is not None:
    print("Novo salário: R$", novo_salario)
