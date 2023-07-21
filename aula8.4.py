class Televisor:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 50

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def trocar_canal(self, novo_canal):
        if novo_canal in self.lista_de_canais:
            self.canal_atual = novo_canal
            print(f"Canal trocado para: {novo_canal}")
        else:
            print("Esse canal não está na lista de canais sintonizados.")

    def sintonizar_novo_canal(self, novo_canal):
        if novo_canal not in self.lista_de_canais:
            self.lista_de_canais.append(novo_canal)
            print(f"Novo canal sintonizado: {novo_canal}")
        else:
            print("Esse canal já está na lista de canais sintonizados.")

televisor_samsung = Televisor(fabricante="Samsung", modelo="Smart TV")

televisor_samsung.sintonizar_novo_canal("Globo")
televisor_samsung.sintonizar_novo_canal("SBT")
televisor_samsung.sintonizar_novo_canal("Record")
televisor_samsung.sintonizar_novo_canal("Band")

televisor_samsung.trocar_canal("SBT")
televisor_samsung.trocar_canal("HBO")  # Esse canal não está na lista de canais sintonizados.

televisor_samsung.aumentar_volume()
televisor_samsung.aumentar_volume()
televisor_samsung.diminuir_volume()

print(f"Fabricante: {televisor_samsung.fabricante}")
print(f"Modelo: {televisor_samsung.modelo}")
print(f"Canal atual: {televisor_samsung.canal_atual}")
print(f"Lista de canais sintonizados: {televisor_samsung.lista_de_canais}")
print(f"Volume: {televisor_samsung.volume}")
