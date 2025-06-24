from pathlib import Path
from pyspark.sql import SparkSession
from analytics.analytics_pipeline import run_pipeline


def test_pipeline():
    spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
    kpis = run_pipeline(Path('data/purchases.csv'), spark)

    assert kpis['top_products'].count() > 0
    assert 'revenue' in kpis['revenue_by_category'].columns
    assert 'total_revenue' in kpis['user_behavior'].columns
    spark.stop()


if __name__ == "__main__":
    test_pipeline()
    print("All tests passed")
