from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from createmetrics.config.ConfigStore import *
from createmetrics.udfs.UDFs import *

def Display(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(lit(True))
