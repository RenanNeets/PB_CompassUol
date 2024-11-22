class Ordenadora:
    def __init__(self,listaBaguncada):
        self.listaBaguncada = listaBaguncada
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
    def ordenacaoDecrecente(self):
        return sorted(self.listaBaguncada, reverse=True)

crecente = Ordenadora([3, 4, 2, 1, 5])
decrecente = Ordenadora([9, 7, 6, 8])
resultadoCrec = crecente.ordenacaoCrescente()
resultadoDescrec = decrecente.ordenacaoDecrecente()

print(resultadoCrec)
print(resultadoDescrec)