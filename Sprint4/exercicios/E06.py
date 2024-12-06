def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values())/ len(conteudo)
    produtosFiltrados = filter(lambda item: item[1]>media, conteudo.items())
    produtosOrdenados = sorted(produtosFiltrados, key=lambda item: item[1])
    return produtosOrdenados
#conjunto de produtos
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))