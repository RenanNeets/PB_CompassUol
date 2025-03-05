def imprimeValor(*args, **kwargs):
    for arg in args:
        print(arg)
    for valor in kwargs.values():
        print(valor)

imprimeValor(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)