import boto3
from datetime import datetime


session = boto3.Session(
    aws_access_key_id='ASIAW5WU46JNG65LJ7UE',
    aws_secret_access_key='K26ImQ35gvflP7eNfQyF0VIGfwOgGw2CXJjd9VQV',
    aws_session_token='IQoJb3JpZ2luX2VjELb//////////wEaCXVzLWVhc3QtMSJIMEYCIQDSGKMkYreJJEXXH76xDRG8QJx4MP69tNdLBYEFyuiWCwIhAL1z9qzIlsXrtwRfopCxeLdIpyRqFZyGEr7eFDPJVC+gKrADCI///////////wEQABoMNDc2MTE0MTIxMzA2Igw2dnxRLJm9cXzljZQqhANZG3rWirl/zA37h2vzpwax3kpRQwQZOB5m366eCguXTacs92rhCkftxCBMnGT9hm66IKhNmKBePgvl/cfX/iyIneVYP3iQ+NtCVBDLmas/qlu8ijbFBJGipJ3L8BBs/yeIE03Qg8pN2u0fHjboJ5yw5ryTiwRT7F7JLDJt1Pyu4Ot75/ei5dekc8fHAamwdfg3FF6akEjqNdj86MMFr/pHCTi3huami//ffWhB6rEPSAVTWqmaJCX7fqjBwXv3geLqhOpOIK5wsWvv0VEJOACwzDKaNiRbcvjVJutgr8MO2tMWcCPo/A+sj5TZZ1gy0k/wX2tBZLjMxAOCk1BNX7yHrITz6+HSD59m9SlLBXUCgAHIqHfrI+oco2pUlikMHuYDYlKcnEh989rimWHJqfx6cWaf9T9u+Orqo39MlnOEQQNL8LrUuNCo3bSIem4GF8cSppNbmhIttfh8QCrPSKj1MOlgVNB54795t6Ly48w0HT03QL9rNzQ7S5XKPPRqLFCh7DDIMN/OyrsGOqUBiuZR4oN4jVl7FcB5b/eDZ9pISHmmGR09ofK4VCymhPtXfNylXivU6+D3yarVSesanTBhUFgYNgEBeV8gUid7hAMQu+1pnWdrBzcQD4ReHlAFHR3nNeSz/63OXEIeBdJMAviY0auhpG6SVtl9HN5/lHWKoGGuecgx9bhIRgZDNVEXyx2VQzeXDOM5GvPvIWtSeccE9+MwxCULRTozeZlS2dZNaneY'
)

with open("movies.csv", 'r', encoding='utf-8') as file:
    moviesData = file.readlines()


with open("series.csv", 'r', encoding='utf-8') as file:
    seriesData = file.readlines()


current_date = datetime.now()
year = current_date.strftime('%Y')
month = current_date.strftime('%m')
day = current_date.strftime('%d')


moviesKey = f"Raw/Local/CSV/Movies/{year}/{month}/{day}/movies.csv"
seriesKey = f"Raw/Local/CSV/Series/{year}/{month}/{day}/series.csv"


client = session.client('s3')

client.create_bucket(Bucket='renan-sprint6-desafio-bucket-2024')

client.upload_file(Filename='movies.csv',
                   Bucket ='renan-sprint6-desafio-bucket-2024',
                   Key=moviesKey)

client.upload_file(Filename='series.csv',
                   Bucket ='renan-sprint6-desafio-bucket-2024',
                   Key=seriesKey)
print("Upload dos arquivos com sucesso")