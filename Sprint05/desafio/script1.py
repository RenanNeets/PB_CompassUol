import boto3
session = boto3.Session(
    aws_access_key_id='ASIAW5WU46JNEKPQZV4E',
    aws_secret_access_key='W2NJ1I4rLMovD4lLeEDbLYeRwPy7J4ihYvDITlTP',
    aws_session_token='IQoJb3JpZ2luX2VjEK///////////wEaCXVzLWVhc3QtMSJHMEUCIHZ7PbBDrcayg6bLxo8/RFAQ09781ogQ2M5k8yK0zzlFAiEA0eb00J9oIF2+bE/3sLuxtFmdTFcgNWazuHCwP6VOYOMqpwMIeBAAGgw0NzYxMTQxMjEzMDYiDI3lIIUpgsakC5GjWyqEA7BfBz01tpsi57jowsi/R0kCl+hTtbCRFTivZA8ZHjrlQfwKnubEo2mpObHSDI5sU9CwlD2omcjsOqyfT8kX8oPfFUUSEf7IPs9VgVa5b3yhkPg7dvMcHImAU2QGOhuhB8m6Qi8VtGxM4UEbHUfpjBWr4efgG0/OXPCch17Reebz9C+2nOCYEgTuWEwACRarHRJgKnxOe0iNQWf7SmsGafW3t5S0G6/UP2EeEGLf0yL9BqWts8k505/o/BvlX3c08T4RC8ryagVVhRKFr5W4mEtT+MMlWYt4EQKNfFCptURUbdZdIC5u8sK/uxFDxVuXts8OKNXiYBSk2kLeE9atBVk9DkqCcavxjAoSYSC2ifJQciocD/2jsMVQjCSpsfK3SzSsI+ub5EghwQqVjunkPDMrZyJg1KcZH0yl6na+llqMF9660BEl9D/RC3q6cHWLpQw94FtMlDBOIxaTRAXj3MWN357oHSNzycl1hR5Lp47/KX3AP7Fgm5sr9jiyG7eLn+VKvMow1N+QuwY6pgGmPek4KhoXFerRRQqpjqRkIigP6bG/o+8roNme7n1LHFIiqr7bzCH9VpS2RtqXZ992SFH37q9VAyF2wHwHdbfgItLdkrc8kM50ftinSKkiZtvbKuxWb0QjqkxEBrzz/GlNrOhGODEm6l3UaCjDv+cN1qh7oKk5PXyQdzJASrCtA/VdG7rTDvF9anZWedeUxsgKRF314alxOglerIr1RuPyZWhCdUya'
)




client = session.client('s3')
client.create_bucket(Bucket='renan-desafio-bucket-2024')

client.upload_file(Filename='dados_abertos_contratos_vigentes_na_acmd_jun_2024.CSV',
                   Bucket ='renan-desafio-bucket-2024',
                   Key='dados-originais')
