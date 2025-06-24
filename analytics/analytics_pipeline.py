from pathlib import Path
from pyspark.sql import SparkSession

from .ingestion import load_purchases
from .transformation import clean, add_revenue
from .kpis import top_products, revenue_by_category, user_behavior


def run_pipeline(path: Path, spark: SparkSession | None = None) -> dict:
    """Execute data analytics pipeline and return KPIs as DataFrames."""
    spark = spark or SparkSession.builder.appName("analytics").getOrCreate()
    df = load_purchases(spark, path)
    df = clean(df)
    df = add_revenue(df)
    return {
        "top_products": top_products(df),
        "revenue_by_category": revenue_by_category(df),
        "user_behavior": user_behavior(df),
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run analytics pipeline")
    parser.add_argument("--file", type=Path, default=Path("data/purchases.csv"))
    args = parser.parse_args()

    spark = SparkSession.builder.master("local[*]").appName("analytics").getOrCreate()
    kpis = run_pipeline(args.file, spark)
    print("Top products:")
    kpis["top_products"].show()
    print("\nRevenue by category:")
    kpis["revenue_by_category"].show()
    print("\nUser behavior:")
    kpis["user_behavior"].show()
    spark.stop()
