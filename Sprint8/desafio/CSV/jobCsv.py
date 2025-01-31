import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import date_format, current_date

args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
#target_path = args['S3_TARGET_PATH']

dadoCsv = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="csv",
    connection_options={"paths": [source_file], "recurse": True},
    format_options={"withHeader": True, "separator": ","}
)
df = dadoCsv.toDF()
dfDataAtual = spark.sql("SELECT current_date() AS data_atual")

# Extrair o ano, mês e dia
ano = dfDataAtual.select(date_format("data_atual", "yyyy").alias("ano")).collect()[0]["ano"]
mes = dfDataAtual.select(date_format("data_atual", "MM").alias("mes")).collect()[0]["mes"]
dia = dfDataAtual.select(date_format("data_atual", "dd").alias("dia")).collect()[0]["dia"]


#target_path = f"s3://renan-desafio-filmes-series-2024/Trusted/Local/Parquet/series/{ano}/{mes}/{dia}/"
target_path = f"s3://renan-desafio-filmes-series-2024/Trusted/Local/Parquet/movies/{ano}/{mes}/{dia}/"


df.repartition(1).write.mode("overwrite") \
    .format("parquet") \
    .save(target_path)
    
job.commit()