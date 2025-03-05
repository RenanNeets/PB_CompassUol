def etapa1(dados):
    maxFilme = 0
    atorFilme = ""
    for linha in dados:
        ator = linha[0]
        try:
            numeroFilme = float(linha[2].strip())
        except ValueError:
            print('Erro etapa 1')
            numeroFilme = 0
        if numeroFilme > maxFilme:
            maxFilme = numeroFilme
            atorFilme = ator
    return atorFilme, maxFilme

def etapa2(dados):
    totalGross = 0
    filmes = 0
    for linha in dados:
        try:
            gross = float(linha[2].strip())
        except ValueError:
            print('Erro etapa 2')
            gross = 0
        totalGross += gross
        filmes +=1
    media = totalGross / filmes if filmes>0 else 0
    return media

def etapa3(dados):
    maiorMedia = 0
    atorMedia = ""
    for linha in dados:
        ator = linha[0]
        mediaFilme = float(linha[3])
        if mediaFilme > maiorMedia:
            maiorMedia = mediaFilme
            atorMedia = ator
    return atorMedia, maiorMedia

def etapa4(dados):
    filmesContagem = {}
    for linha in dados:
        filme = linha[4].strip()
        if filme in filmesContagem:
            filmesContagem[filme] += 1
        else:
            filmesContagem[filme] = 1
    filmesOrdenados = sorted(filmesContagem.items(), key = lambda x: (-x[1], x[0]))
    return filmesOrdenados

def etapa5(dados):
    receitaAtores = []
    for linha in dados:
        try:
            ator = linha[0].strip()
            receita = float(linha[1])
        except ValueError:
            print('Erro etapa 5')
            continue
        receitaAtores.append((ator,receita))
    return receitaAtores


with open('./Sprint3/exercicios/pythonII/actors.csv', 'r') as arquivos:
        linhas = arquivos.readlines()
cabecalho = linhas[0].strip().split(',')
dados = [linha.strip().split(',') for linha in linhas[1:]]

ator, filmes = etapa1(dados)
with open('./Sprint3/exercicios/pythonII/etapa-1.txt', 'w') as arquivo:
        arquivo.write(f"{ator} - {filmes} filmes")

media = etapa2(dados)
with open('./Sprint3/exercicios/pythonII/etapa-2.txt', 'w') as arquivo:
    arquivo.write(f"{media:.2f}")

ator, media = etapa3(dados)
with open('./Sprint3/exercicios/pythonII/etapa-3.txt', 'w') as arquivo:
    arquivo.write(f"{ator} - {media:.2f}")

filmes = etapa4(dados)
with open('./Sprint3/exercicios/pythonII/etapa-4.txt', 'w') as arquivo:
    for filme,count in filmes:
        arquivo.write(f"O filme {filme} aparece {count} vez(es) no dataset\n")

atores = etapa5(dados)
with open('./Sprint3/exercicios/pythonII/etapa-5.txt', 'w') as arquivo:
    for ator, receita in atores:
        arquivo.write(f"{ator} - {receita:.2f} \n")