import json
import requests
import boto3
from datetime import datetime
from time import sleep

def lambda_handler(event, context):

    key = "CHAVE AQUIII"


    url = (
        f"https://api.themoviedb.org/3/discover/tv?"
        f"api_key={key}&language=pt-BR&sort_by=popularity.desc"
        f"&with_origin_country=BR&with_genres=35&"
        f"first_air_date.gte=1980-01-01&first_air_date.lte=2000-12-31"
    )
    seriesBrasileiras = []


    for pagina in range(1, 6):
        resposta = requests.get(f"{url}&page={pagina}")
        # Vê se a url funcionou
        if not resposta.ok:
            break
        data = resposta.json()

        for tvShow in data.get("results", []):
            id = tvShow["id"] 

            external_ids_url = f"https://api.themoviedb.org/3/tv/{id}/external_ids?api_key={key}"
            external_ids_resposta = requests.get(external_ids_url)
            if external_ids_resposta.ok:
                external_ids = external_ids_resposta.json()
                imdb_id = external_ids.get("imdb_id", "N/A")

            extra = f"https://api.themoviedb.org/3/tv/{id}?api_key={key}&language=pt-BR"
            extraResposta = requests.get(extra)
            # Vê se a 2° url funcionou
            if extraResposta.ok:
                detalhes = extraResposta.json()
                temporadas = detalhes.get("number_of_seasons", "N/A")
                episodios = detalhes.get("number_of_episodes", "N/A")
                status = detalhes.get("status", "N/A")
                idioma_original = detalhes.get("original_language", "N/A")
                popularidade = detalhes.get("popularity", "N/A")
                generos = ", ".join([g["name"] for g in detalhes.get("genres", [])])
                produtoras = ", ".join([p["name"] for p in detalhes.get("production_companies", [])])
                paises_producao = ", ".join([c["name"] for c in detalhes.get("production_countries", [])])
                poster_url = f"https://image.tmdb.org/t/p/w500{detalhes.get('poster_path')}" if detalhes.get("poster_path") else "N/A"
            else:
                temporadas = episodios = status = idioma_original = popularidade = generos = produtoras = paises_producao = poster_url = "N/A"



            creditosUrl = f"https://api.themoviedb.org/3/tv/{id}/credits?api_key={key}&language=pt-BR"
            creditos = requests.get(creditosUrl)
            #Vê se a 3° url funcionou
            if creditos.ok:
                creditosDados = creditos.json()
                dubladores = [
                    membro["name"] for membro in creditosDados.get("cast", [])
                    if membro.get("known_for_department") == "Acting"
                ]
            else:
                dubladores = ["Informação indisponível"]
            seriesBrasileiras.append({
                "IMDB ID": imdb_id,
                "Título": tvShow.get("name", "N/A"),
                "Data de estreia": tvShow.get("first_air_date", "N/A"),
                "Visão geral": tvShow.get("overview", "N/A"),
                "Votos": tvShow.get("vote_count", 0),
                "Média de votos": tvShow.get("vote_average", 0.0),
                "Número de Temporadas": temporadas,
                "Número de Episódios": episodios,
                "Status": status,
                "Idioma Original": idioma_original,
                "Popularidade": popularidade,
                "Gêneros": generos,
                "Produtoras": produtoras,
                "Países de Produção": paises_producao,
                "Atores": ", ".join(dubladores) if dubladores else "Informação indisponível",
            })
        sleep(1)
    save_to_s3(seriesBrasileiras)
    return {"status": "success"}

def save_to_s3(data ):
    s3 = boto3.client('s3')

    current_date = datetime.now()
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')

    seriesKey = f"Raw/TMDB/JSON/{year}/{month}/{day}/SeriesBrasileirasComedia.json"

    arquivo = "/tmp/SeriesBrasileirasComedia.json"
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


    s3.upload_file(Filename=arquivo,
                   Bucket ='renan-desafio-filmes-series-2024',
                   Key=seriesKey)
    return {"status": "success_upload"}

