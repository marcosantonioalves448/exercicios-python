def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    estatura = float(input("Digite a estatura do aluno (em metros): "))
    peso = float(input("Digite o peso do aluno (em quilogramas): "))
    return {
        "nome": nome,
        "estatura": estatura,
        "peso": peso,
        "imc": calcular_imc(peso, estatura)
    }

def main():
    print("Cadastro de Alunos\n")

    alunos = []
    numero_alunos = int(input("Digite o número de alunos que deseja cadastrar: "))

    for i in range(numero_alunos):
        print(f"\nAluno {i + 1}:")
        aluno = cadastrar_aluno()
        alunos.append(aluno)

    print("\nRelatório de Alunos (ordenados pelo nome):\n")
    for aluno in sorted(alunos, key=lambda x: x["nome"]):
        print(f"Nome: {aluno['nome']}, IMC: {aluno['imc']:.2f}")

if __name__ == "__main__":
    main()
