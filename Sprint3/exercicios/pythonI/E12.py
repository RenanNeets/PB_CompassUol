def my_map(list, f):
    resultado = []
    for x in list:
        resultado.append(f(x))
    return resultado

def power_2(x):
    return x **2
listaEntrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resuntadoFinal = my_map(listaEntrada, power_2)
print(resuntadoFinal)