import json
import csv
import boto3
import requests
from datetime import datetime

def lambda_handler(event, context):
    bucket_name = "renan-desafio-filmes-series-2024"
    file_key = "Raw/Local/CSV/Series/2025/01/02/series.csv"

    tmdb_api_key = "CHAVE AQUIII"

    s3_client = boto3.client('s3')

    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        csv_content = response['Body'].read().decode('utf-8')

        rows = []
        csv_reader = csv.DictReader(csv_content.splitlines())
        for row in csv_reader:
            if len(rows) >= 100:
                break 
            imdb_id = row.get("id", "N/A")
            titulo_original = row.get("tituloOriginal", "N/A")
            nota_media = float(row.get("notaMedia", 0.0))
            numero_votos = int(row.get("numeroVotos", 0))
            genero = row.get("genero", "N/A")
            atores = row.get("nomeArtista", "N/A")

            api_data = complemento_tmdb(imdb_id, tmdb_api_key)

            data_estreia = api_data.get("first_air_date", "N/A")
            if data_estreia != "N/A":
                data_estreia_date = datetime.strptime(data_estreia, "%Y-%m-%d")
            else:
                continue
            if "comedy" in genero.lower() and datetime(1980, 1, 1) <= data_estreia_date <= datetime(2000, 12, 31):
                rows.append({
                    "IMDB ID": imdb_id,
                    "Título": titulo_original,
                    "Data de estreia": data_estreia,
                    "Visão geral": api_data.get("overview", "N/A"),
                    "Votos": numero_votos,
                    "Média de votos": nota_media,
                    "Número de Temporadas": api_data.get("number_of_seasons", "N/A"),
                    "Número de Episódios": api_data.get("number_of_episodes", "N/A"),
                    "Status": api_data.get("status", "N/A"),
                    "Idioma Original": api_data.get("original_language", "N/A"),
                    "Popularidade": api_data.get("popularity", "N/A"),
                    "Gêneros": genero,
                    "Produtoras": ", ".join([p["name"] for p in api_data.get("production_companies", [])]),
                    "Países de Produção": ", ".join([c["name"] for c in api_data.get("production_countries", [])]),
                    "Atores": atores,
                })


        save_to_s3(rows)

        return {
            "statusCode": 200,
            "body": {
                "message": "Arquivo CSV processado e informações complementadas com sucesso!",
                "total_registros": len(rows)
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {
                "error": str(e),
                "message": "Erro ao processar o arquivo CSV do S3 ou buscar informações da API."
            }
        }

def complemento_tmdb(imdb_id, api_key):
    #Complemento com TMDB
    try:
        url = f"https://api.themoviedb.org/3/find/{imdb_id}?api_key={api_key}&language=pt-BR&external_source=imdb_id"
        response = requests.get(url)
        if response.ok:
            results = response.json().get("tv_results", [])
            if results:
                tv_id = results[0]["id"]
                details_url = f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={api_key}&language=pt-BR"
                details_response = requests.get(details_url)
                if details_response.ok:
                    return details_response.json()
        return {}
    except Exception as e:
        print(f"Erro ao buscar dados do TMDB para {imdb_id}: {e}")
        return {}

def save_to_s3(data):
    s3 = boto3.client('s3')

    current_date = datetime.now()
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')

    series_key = f"Processed/CSV/{year}/{month}/{day}/SeriesBrasileirasComedia.json"

    arquivo = "/tmp/SeriesBrasileirasComedia.json"
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    s3.upload_file(Filename=arquivo,
                   Bucket='renan-desafio-filmes-series-2024',
                   Key=series_key)
    return {"status": "success_upload"}
