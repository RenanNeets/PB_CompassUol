import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as F

# Argumentos do AWS Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos para os arquivos no S3
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lê o arquivo CSV do S3 usando AWS Glue
df = glueContext.create_dynamic_frame_from_options(
    "s3",
    {
        "paths": [
            source_file
        ]
    },
    "csv",
    {"withHeader": True, "separator": ","}
).toDF()
df.printSchema()


dfUpper = df.withColumn("nome", F.upper(F.col("nome")))
print(f"Número total de linhas: {dfUpper.count()}")


contagem = (dfUpper
                     .groupBy("ano", "sexo")
                     .count()
                     .orderBy(F.col("ano").desc()))
print("Contagem de nomes, ano e sexo:")
contagem.show()


femininoRegistrado = (dfUpper.filter(F.col("sexo") == "F")
                            .groupBy("ano", "nome")
                            .count()
                            .orderBy(F.col("count").desc())
                            .first())
print(f"Nome feminino mais registrado: {femininoRegistrado['nome']}, Ano: {femininoRegistrado['ano']}")


masculinoRegistrado = (dfUpper.filter(F.col("sexo") == "M")
                             .groupBy("ano", "nome")
                             .count()
                             .orderBy(F.col("count").desc())
                             .first())
print(f"Nome masculino mais registrado: {masculinoRegistrado['nome']}, Ano: {masculinoRegistrado['ano']}")


totalAno = (dfUpper
                 .groupBy("ano")
                 .count()
                 .orderBy("ano")
                 .limit(10))
print("Total ano:")
totalAno.show()


dfUpper.write.mode("overwrite")\
             .format("json")\
             .partitionBy("sexo", "ano")\
             .save(output_path)

glueContext.write_dynamic_frame.from_options(
    frame=glueContext.create_dynamic_frame.from_dataframe(ano1934, glueContext),
    connection_type="s3",
    connection_options={"path": target_path},
    format="parquet"
)

job.commit()
