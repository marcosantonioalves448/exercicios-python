class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv
    
    def aumenta_volume(self, valor):
        self.tv.aumentar_volume(valor)
    
    def diminui_volume(self, valor):
        self.tv.diminuir_volume(valor)
    
    def troca_canal(self, canal):
        self.tv.trocar_canal(canal.lower())
    
    def sintoniza_canal(self, canal):
        self.tv.sintonizar_novo_canal(canal.lower())

tv1 = Televisor('LG', 'Teste')
tv1.sintonizar_novo_canal('SBT')
tv1.sintonizar_novo_canal('Globo')
controle = ControleRemoto(tv1)

controle.aumenta_volume(90)
controle.sintoniza_canal('HBO')
controle.troca_canal('SBT')

print(tv1.canal_atual)  