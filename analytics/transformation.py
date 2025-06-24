from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean(df: DataFrame) -> DataFrame:
    """Remove duplicates and normalize text fields."""
    return (
        df.dropDuplicates()
        .withColumn("category", F.lower(F.col("category")))
        .withColumn("payment_method", F.lower(F.col("payment_method")))
    )


def add_revenue(df: DataFrame) -> DataFrame:
    """Add revenue column derived from quantity and price."""
    return df.withColumn("revenue", F.col("quantity") * F.col("price"))
