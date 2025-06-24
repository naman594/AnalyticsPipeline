from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def top_products(df: DataFrame, top_n: int = 3) -> DataFrame:
    """Top selling products by revenue."""
    return (
        df.groupBy("product_id", "product_name")
        .agg(F.sum("revenue").alias("revenue"))
        .orderBy(F.desc("revenue"))
        .limit(top_n)
    )


def revenue_by_category(df: DataFrame) -> DataFrame:
    """Total revenue for each category."""
    return df.groupBy("category").agg(F.sum("revenue").alias("revenue"))


def user_behavior(df: DataFrame) -> DataFrame:
    """Purchase counts and revenue per user."""
    return (
        df.groupBy("user_id")
        .agg(
            F.sum("quantity").alias("total_purchases"),
            F.sum("revenue").alias("total_revenue")
        )
    )
