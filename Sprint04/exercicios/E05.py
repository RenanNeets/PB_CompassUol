def processarNotas(arquivoCSV: str):
    with open('estudantes.csv','r') as arquivo:
        linhas = arquivo.readlines()
    estudantes = map(lambda linha: linha.strip().split(','),linhas)
    relatorio = sorted(
        map(
            lambda estudante:{
                "nome": estudante[0],
                "notas": sorted(map(int,estudante[1:]), reverse=True)[:3],
            },
            estudantes
        ),
        key=lambda x: x["nome"]
    )
    for estudante in relatorio:
        nome = estudante["nome"]
        notas = estudante["notas"]
        media = round(sum(notas)/3, 2)
        print(f"Nome: {nome} Notas: {notas} Média: {media}")
processarNotas('estudantes.csv')