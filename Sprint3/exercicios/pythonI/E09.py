nomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobrenomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, nome in enumerate(nomes):
    sobrenome = sobrenomes[i]
    idade = idades[i]
    print(f"{i} - {nome} {sobrenome} está com {idade} anos")