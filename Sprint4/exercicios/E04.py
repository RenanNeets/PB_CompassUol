def calcular_valor_maximo(operador,rodando) -> float:
    resultado = map(
        lambda operacao: eval(f"{operacao[1][0]} {operacao[0]} {operacao[1][1]}"),
        zip(operador, rodando)
    )
    return max(resultado)
operador = ['+', '-', '*', '/', '+']
rodando = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
print(calcular_valor_maximo(operador, rodando))