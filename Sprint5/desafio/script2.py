import pandas as pd
import boto3
from datetime import datetime
#Credenciais
session = boto3.Session(
    aws_access_key_id='ASIAW5WU46JNEKPQZV4E',
    aws_secret_access_key='W2NJ1I4rLMovD4lLeEDbLYeRwPy7J4ihYvDITlTP',
    aws_session_token='IQoJb3JpZ2luX2VjEK///////////wEaCXVzLWVhc3QtMSJHMEUCIHZ7PbBDrcayg6bLxo8/RFAQ09781ogQ2M5k8yK0zzlFAiEA0eb00J9oIF2+bE/3sLuxtFmdTFcgNWazuHCwP6VOYOMqpwMIeBAAGgw0NzYxMTQxMjEzMDYiDI3lIIUpgsakC5GjWyqEA7BfBz01tpsi57jowsi/R0kCl+hTtbCRFTivZA8ZHjrlQfwKnubEo2mpObHSDI5sU9CwlD2omcjsOqyfT8kX8oPfFUUSEf7IPs9VgVa5b3yhkPg7dvMcHImAU2QGOhuhB8m6Qi8VtGxM4UEbHUfpjBWr4efgG0/OXPCch17Reebz9C+2nOCYEgTuWEwACRarHRJgKnxOe0iNQWf7SmsGafW3t5S0G6/UP2EeEGLf0yL9BqWts8k505/o/BvlX3c08T4RC8ryagVVhRKFr5W4mEtT+MMlWYt4EQKNfFCptURUbdZdIC5u8sK/uxFDxVuXts8OKNXiYBSk2kLeE9atBVk9DkqCcavxjAoSYSC2ifJQciocD/2jsMVQjCSpsfK3SzSsI+ub5EghwQqVjunkPDMrZyJg1KcZH0yl6na+llqMF9660BEl9D/RC3q6cHWLpQw94FtMlDBOIxaTRAXj3MWN357oHSNzycl1hR5Lp47/KX3AP7Fgm5sr9jiyG7eLn+VKvMow1N+QuwY6pgGmPek4KhoXFerRRQqpjqRkIigP6bG/o+8roNme7n1LHFIiqr7bzCH9VpS2RtqXZ992SFH37q9VAyF2wHwHdbfgItLdkrc8kM50ftinSKkiZtvbKuxWb0QjqkxEBrzz/GlNrOhGODEm6l3UaCjDv+cN1qh7oKk5PXyQdzJASrCtA/VdG7rTDvF9anZWedeUxsgKRF314alxOglerIr1RuPyZWhCdUya'
)

s3 = session.resource('s3')
client = session.client('s3')

#Baixar o arquivo do S3
client.download_file(Bucket='renan-desafio-bucket-2024',
                     Key='dados-originais',
                      Filename='contratos_vigentes_na_acmd.CSV')



# Normalização

df = pd.read_csv("contratos_vigentes_na_acmd.CSV", encoding='latin-1', sep=';')

df.to_csv("contratos_vigentes_na_acmd.txt", sep='\t', index=False)
df_txt = pd.read_csv("contratos_vigentes_na_acmd.txt", sep='\t')

df_txt.to_csv("contratos_vigentes_ACMD.csv", index=False)

print("Conversão completa")

df = pd.read_csv("contratos_vigentes_ACMD.csv", encoding='utf-8', sep=',')
df.rename(columns={'RELAÇÃO DE CONTRATOS VIGENTES NA ADMINISTRAÇÃO CENTRAL DO MINISTÉRIO DA DEFESA.  ref.: jun.24': 'CONTRATO',
                   'Unnamed: 1':'ANO',
                   'Unnamed: 2':'EMPRESA',
                   'Unnamed: 3':'CNPJ',
                   'Unnamed: 4':'OBJETO',
                   'Unnamed: 5':'TIPO',
                   'Unnamed: 6':'INÍCIO',
                   'Unnamed: 7':'ENCERRAMENTO',
                   'Unnamed: 8':'VALOR ANUAL',
                   }, inplace=True)
df = df.iloc[1:]
print(df)
df.to_csv("contratos_vigentes_ACMD.csv", index=False)

print("Conversão completa2")

# Upload do arquivo nomalizado
client.upload_file(Filename='contratos_vigentes_ACMD.CSV',
                   Bucket ='renan-desafio-bucket-2024',
                   Key='dados-normalizados')


# Topíco 4 
df = pd.read_csv("contratos_vigentes_ACMD.csv", encoding='utf-8', sep=',')

conrversaoMonetaria = df['VALOR ANUAL'].str.replace('R$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
df['VALOR ANUAL'] =  conrversaoMonetaria
df['VALOR ANUAL'] = pd.to_numeric(df['VALOR ANUAL'], errors='coerce')


#4.1
condicao = ((df['ANO'] == 2023) & (df['CNPJ'] == df['CNPJ']) )
dfFiltrado = df[condicao].copy()
# print(dfFiltrado)

#4.2
dfAgg1 = df.groupby((df['ANO'] == 2023)).size()
dfAgg1.index = dfAgg1.index.map({True: 'Dentro de 2023:', False: 'Fora de 2023:'})
dfAgg2 = df['VALOR ANUAL'].max()
dfAgregacao = f"Primeira Agregação: \n{dfAgg1} \nSegunda Agregação, mostrando o valor mais caro: \n{dfAgg2}"
# print(dfAgregacao)

#4.3
df['VALOR ANUAL ALTOS'] = df['VALOR ANUAL'] > 50000
#print(df[['VALOR ANUAL', 'VALOR ANUAL ALTOS']])

#4.4

df['DATA ENCERRAMENTO'] = pd.to_datetime(df['ENCERRAMENTO'], format='%d/%m/%Y', errors='coerce')
df['DATA ENCERRAMENTO'] = df['DATA ENCERRAMENTO'].fillna('Indeterminado')
#print(df['DATA ENCERRAMENTO'])

#4.5
df['ANO ENCERRAMENTO'] = pd.to_datetime(df['ENCERRAMENTO'], format='%d/%m/%Y', errors='coerce').dt.year
df['ANO ENCERRAMENTO'] = df['ANO ENCERRAMENTO'].fillna('Indeterminado')
#print(df['ANO ENCERRAMENTO'])

#4.6
df.columns = df.columns.str.strip().str.lower()
#print(df.columns)

df.to_csv("contratos_vigentes_ACMD_analisados.csv", index=False)


#Upload

client.upload_file(Filename='contratos_vigentes_ACMD_analisados.csv',
                   Bucket ='renan-desafio-bucket-2024',
                   Key='dados-analisados')