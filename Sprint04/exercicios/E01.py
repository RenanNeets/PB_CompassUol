with open('number.txt', 'r') as file:
    listaNumeros = map(int, file.readlines())

pares = filter(lambda x: x % 2 == 0, listaNumeros)
paresOrdenados = sorted(pares, reverse=True)
paresMaiores = paresOrdenados[:5]
somaMaiores = sum(paresMaiores)

print(paresMaiores)
print(somaMaiores)
