class Bola:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def imprimir_cor(self):
        print(f"A cor da bola é {self.cor}")

    def calcular_area(self):
        area = 4 * 3.14 * self.raio * self.raio
        return area

    def calcular_volume(self):
        volume = (4 * 3.14 * self.raio * self.raio * self.raio) / 3
        return volume

bola_vermelha = Bola(cor="vermelho", raio=5)

bola_vermelha.imprimir_cor()

area_da_bola = bola_vermelha.calcular_area()
print(f"A área da bola é: {area_da_bola}")

volume_da_bola = bola_vermelha.calcular_volume()
print(f"O volume da bola é: {volume_da_bola}")
