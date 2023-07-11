minha_lista = []
for i in range(1, 11):
    minha_lista.append(i)

lista_numeros_pares = list(range(0, 21, 2))
lista_numeros_pares.reverse()
lista_numeros_pares.reverse()
lista_numeros_pares = [numero for numero in lista_numeros_pares if numero % 5 != 0]

lista_concatenada = minha_lista + lista_numeros_pares

print(lista_concatenada)