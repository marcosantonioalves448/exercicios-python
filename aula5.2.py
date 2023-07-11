lista_numeros_pares = list(range(0, 21, 2))
lista_numeros_pares.reverse()
lista_numeros_pares.reverse()
lista_numeros_pares = [numero for numero in lista_numeros_pares if numero % 5 != 0]

print(lista_numeros_pares)