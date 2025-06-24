from pathlib import Path
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as F


def load_purchases(spark: SparkSession, path: Path) -> DataFrame:
    """Read purchase data from CSV."""
    df = (
        spark.read.option("header", True)
        .option("inferSchema", True)
        .csv(str(path))
    )
    return df.withColumn("timestamp", F.to_timestamp("timestamp"))
