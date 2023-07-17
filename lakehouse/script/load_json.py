import pyspark
from delta import *

def load_json():
    # Step 1: Initialize Spark session
    builder = pyspark.sql.SparkSession.builder.appName("receipt") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

    spark = configure_spark_with_delta_pip(builder).getOrCreate()

    # Step 2: Read data from another folder into a DataFrame
    source_folder = "../../data/receipt-data/json/"
    df = spark.read.option("multiline","true").json(source_folder)

    # Step 3: Write data to Delta Lake
    target_folder = "../storage/receipt-json-delta/"
    df.write.format("delta").mode("overwrite").save(target_folder)

    print("==========Json Loading Complete!!==========")