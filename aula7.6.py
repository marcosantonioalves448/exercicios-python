def main():
    semana = {
        'segunda': ['Aula de Matemática', 'Aula de História'],
        'terça': ['Aula de Ciências', 'Aula de Português'],
        'quarta': ['Aula de Geografia', 'Aula de Inglês'],
        'quinta': ['Aula de Física', 'Aula de Educação Física'],
        'sexta': ['Aula de Química', 'Aula de Artes'],
        'sábado': [],
        'domingo': []
    }

    print("Aulas da semana:\n")
    for dia, aulas in semana.items():
        print(f"{dia.capitalize()}: {', '.join(aulas) or 'Sem aulas'}")

if __name__ == "__main__":
    main()
