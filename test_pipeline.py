import pandas as pd
from analytics.analytics_pipeline import load_data, clean_data, transform_data, kpi_top_products, kpi_revenue_by_category, kpi_user_behavior


def test_pipeline():
    df = load_data('data/purchases.csv')
    df = clean_data(df)
    df = transform_data(df)

    top_products = kpi_top_products(df, top_n=1)
    assert not top_products.empty

    revenue_by_category = kpi_revenue_by_category(df)
    assert 'revenue' in revenue_by_category.columns

    user_behavior = kpi_user_behavior(df)
    assert 'total_revenue' in user_behavior.columns

if __name__ == "__main__":
    test_pipeline()
    print('All tests passed')
