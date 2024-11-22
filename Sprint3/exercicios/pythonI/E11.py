import json
with open('person.json', encoding='utf-8') as pessoa:
    dados = json.load(pessoa)
print(dados)