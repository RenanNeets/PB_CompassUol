def conta_vogais(texto:str)-> int:
    vogais = 'aeiouAEIOU'
    vogaisApenas = filter(lambda char: char in vogais, texto)
    return len(list(vogaisApenas))

texto = "Exemplo simples"
print(conta_vogais(texto))