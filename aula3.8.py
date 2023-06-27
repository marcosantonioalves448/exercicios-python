nome_corretor = input("Digite o nome do corretor: ")
quantidade_imoveis = int(input("Digite a quantidade de imóveis vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: "))

salario_base = 1500.00
comissao_por_imovel = 200.00
porcentagem_comissao = 0.05

comissao_total = quantidade_imoveis * comissao_por_imovel
valor_comissao = valor_vendas * porcentagem_comissao

salario_final = salario_base + comissao_total + valor_comissao

print("O salário final de", nome_corretor, "é: R$", salario_final)
