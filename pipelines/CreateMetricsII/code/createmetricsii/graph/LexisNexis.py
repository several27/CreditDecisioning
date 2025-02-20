from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from createmetricsii.config.ConfigStore import *
from createmetricsii.udfs.UDFs import *

def LexisNexis(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("json")\
        .schema(
          StructType([
            StructField("balance", LongType(), True), StructField("lender_name", StringType(), True), StructField("loan_id", LongType(), True), StructField("monthly_loan_amount", StringType(), True), StructField("name", StringType(), True), StructField("past_due", LongType(), True), StructField("processor", StringType(), True), StructField("term", StringType(), True)
        ])
        )\
        .load("dbfs:/Prophecy/finserv/ingest/BNPL/bnpl.json")
