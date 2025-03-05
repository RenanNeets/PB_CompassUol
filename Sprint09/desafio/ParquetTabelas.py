import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import SparkSession
from pyspark.sql.functions import split, row_number,explode, col, to_date, year, month, dayofmonth
from pyspark.sql.window import Window


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_file = args['S3_TARGET_PATH']

# Inicializa a sessão Spark 
dadoParquet = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [source_file], "recurse": True}
)
df = dadoParquet.toDF()
df = df.withColumnRenamed("Título","titulo").orderBy("titulo")
df = df.withColumnRenamed("Dubladores","Atores")
#df.show()

# Criando dimensão de data
df_dim_data = df.select("titulo",
    to_date("Data_de_estreia", "yyyy-MM-dd").alias("full_date")).distinct()
df_dim_data = df_dim_data.withColumn("year", year("full_date")).withColumn("month", month("full_date")).withColumn("day", dayofmonth("full_date"))
df_dim_data = df_dim_data.withColumn("data_key", row_number().over(Window.orderBy(col("titulo").asc_nulls_last())))

# Criando dimensão de atores
df_dim_atores = df.select(
    "titulo",
    explode(split(col("Atores"), ",\s*")).alias("nome")
).distinct()

df_dim_atores = df_dim_atores.withColumn("ator_key", row_number().over(Window.orderBy("titulo")))

# Criando dimensão Paises de Produção
df_dim_paises_de_producao = df.select("titulo",
    explode(split(col("Países_de_Produção"), ",\s*")).alias("paises_producao")
).distinct()
df_dim_paises_de_producao = df_dim_paises_de_producao.withColumn("paises_de_producao_key", row_number().over(Window.orderBy("titulo")))

# Criando dimensão Generos
df_dim_generos = df.select("titulo",
    explode(split(col("Gêneros"), ",\s*")).alias("generos")
).distinct()
df_dim_generos = df_dim_generos.withColumn("generos_key", row_number().over(Window.orderBy("titulo")))
print(df_dim_generos)

# Criando dimensão Produtora
df_dim_produtora = df.select("titulo",
    explode(split(col("Produtoras"), ",\s*")).alias("produtoras")
).distinct()
df_dim_produtora = df_dim_produtora.withColumn("produtora_key", row_number().over(Window.orderBy("titulo")))
print(df_dim_produtora)

# Criando dimensão Descrição
df_dim_descricao = df.select("titulo",
    split(col("Status"), ",\\s*").alias("status"),
    split(col("Idioma_Original"), ",\\s*").alias("idioma_original"),
).distinct()
df_dim_descricao = df_dim_descricao.withColumn("descricao_key", row_number().over(Window.orderBy("titulo")))

# Criando Fato Séries
df_fato_series = df.join(df_dim_atores, "titulo") \
            .join(df_dim_generos, "titulo") \
            .join(df_dim_descricao, "titulo") \
            .join(df_dim_paises_de_producao, "titulo") \
            .join(df_dim_data, "titulo") \
            .join(df_dim_produtora, "titulo") \
            .select(
                df_dim_atores.ator_key,
                df_dim_paises_de_producao.paises_de_producao_key,
                df_dim_produtora.produtora_key,
                df_dim_generos.generos_key,
                df_dim_descricao.descricao_key,
                df_dim_data.data_key,
                df.Votos.cast("integer"),
                df["Média_de_votos"].cast("double"),
                df.Popularidade.cast("double")
            )

# Removendo coluna de ligação
df_dim_atores = df_dim_atores.drop('titulo')
df_dim_data = df_dim_data.drop('titulo')
df_dim_paises_de_producao = df_dim_paises_de_producao.drop('titulo')
df_dim_generos = df_dim_generos.drop('titulo')
df_dim_produtora = df_dim_produtora.drop('titulo')

#Caminhos
atores_path = f"{target_file}Refined/DimAtores/dim-atores"
data_path = f"{target_file}Refined/DimData/dim-data"
paises_de_producao_path = f"{target_file}Refined/DimPaisesProducao/dim-paises-de-producao"
genero_path = f"{target_file}Refined/DimGenero/dim-genero"
produtora_path = f"{target_file}Refined/DimProdutora/dim-produtora"
descricao_path = f"{target_file}Refined/DimDescricao/dim-descricao"
fato_path = f"{target_file}Refined/FatoSeries/dim-fato-series"

df_dim_atores.write.mode("overwrite").parquet(atores_path)
df_dim_data.write.mode("overwrite").parquet(data_path)
df_dim_paises_de_producao.write.mode("overwrite").parquet(paises_de_producao_path)
df_dim_generos.write.mode("overwrite").parquet(genero_path)
df_dim_produtora.write.mode("overwrite").parquet(produtora_path)
df_dim_descricao.write.mode("overwrite").parquet(descricao_path)
df_fato_series.write.mode("overwrite").parquet(fato_path)




job.commit()