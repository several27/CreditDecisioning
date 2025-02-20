from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from importdataoption.config.ConfigStore import *
from importdataoption.udfs.UDFs import *

def RestAPIEnrich_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from prophecy.udfs import get_rest_api
    requestDF = in0.withColumn(
        "api_output",
        get_rest_api(
          to_json(
            struct(
              lit("GET").alias("method"), 
              lit(
                  "https://raw.githubusercontent.com/atbida/terraform-databricks-lakehouse-blueprints/main/industry/fsi/data/TransUnionFICO"
                )\
                .alias("url"), 
              lit("{\"version\":\"1.0\", \"encoding\":\"UTF-8\"}").alias("headers")
            )
          ),
          lit("")
        )
    )

    return requestDF
