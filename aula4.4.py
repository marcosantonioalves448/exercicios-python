nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
nota3 = float(input('Informe a terceira nota:'))
notas_media = (nota1+nota2+nota3)/3
if(notas_media >= 6):
    print('Aprovado com média de: ', notas_media)
else:
    print('Reprovado com média de: ', notas_media)