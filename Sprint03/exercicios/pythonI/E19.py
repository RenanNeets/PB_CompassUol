import random

random_list = random.sample(range(500),50)

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

listaOrdenada = sorted(random_list)

valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)

quantidade = len(listaOrdenada)
if quantidade % 2 ==1:
    mediana = listaOrdenada[quantidade//2]
else:
    mediana = (listaOrdenada[quantidade//2 -1] + listaOrdenada[quantidade//2]) / 2
print(
    f"Media: {media:.1f}, Mediana: {mediana:.1f}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}"
      )