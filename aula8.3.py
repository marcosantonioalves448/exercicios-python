class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas_trabalhadas = {}
        self.salario_por_hora = {}

    def adicionar_horas_trabalhadas(self, mes, horas):
        self.horas_trabalhadas[mes] = horas

    def adicionar_salario_por_hora(self, mes, salario_hora):
        self.salario_por_hora[mes] = salario_hora

    def calcular_salario_mensal(self, mes):
        if mes not in self.horas_trabalhadas or mes not in self.salario_por_hora:
            return 0

        horas_trabalhadas = self.horas_trabalhadas[mes]
        salario_hora = self.salario_por_hora[mes]
        salario_mensal = horas_trabalhadas * salario_hora
        return salario_mensal

funcionario_joao = Funcionario(nome="João", email="joao@gmail.com")

funcionario_joao.adicionar_horas_trabalhadas(mes="julho", horas=160)
funcionario_joao.adicionar_salario_por_hora(mes="julho", salario_hora=25)

salario_julho = funcionario_joao.calcular_salario_mensal(mes="julho")
print(f"Salário de João em julho: R${salario_julho}")
