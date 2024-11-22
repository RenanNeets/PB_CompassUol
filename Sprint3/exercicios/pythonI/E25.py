class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "azul"

aviao1 = Aviao("BOIENG456", 1500, 400)
aviao2 = Aviao("Embrar Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)
avioes = [aviao1,aviao2,aviao3]
for aviao in avioes:
    print(
        f"Avião modelo {aviao.modelo}, velocidade máxima {aviao.velocidade_maxima}, capacidade {aviao.capacidade}, cor {aviao.cor}"
        )
    