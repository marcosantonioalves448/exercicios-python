class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def calcular_area(self):
        area = self.lado_a * self.lado_b
        return area

retangulo = Retangulo(lado_a=5, lado_b=7)

area_do_retangulo = retangulo.calcular_area()
print(f"A área do retângulo é: {area_do_retangulo}")