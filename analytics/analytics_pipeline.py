import pandas as pd
from pathlib import Path


def load_data(path: Path) -> pd.DataFrame:
    """Load purchase data from a CSV file."""
    df = pd.read_csv(path, parse_dates=['timestamp'])
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean purchase data."""
    df = df.drop_duplicates()
    df['category'] = df['category'].str.lower()
    df['payment_method'] = df['payment_method'].str.lower()
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Add revenue column and other derived fields."""
    df['revenue'] = df['quantity'] * df['price']
    return df


def kpi_top_products(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """Return top selling products by revenue."""
    return (
        df.groupby(['product_id', 'product_name'])['revenue']
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )


def kpi_revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Return total revenue for each product category."""
    return df.groupby('category')['revenue'].sum().reset_index()


def kpi_user_behavior(df: pd.DataFrame) -> pd.DataFrame:
    """Return purchase counts and revenue per user."""
    return (
        df.groupby('user_id')
        .agg(total_purchases=('quantity', 'sum'), total_revenue=('revenue', 'sum'))
        .reset_index()
    )


def run_pipeline(path: Path) -> dict:
    """Execute data analytics pipeline and return KPIs."""
    df = load_data(path)
    df = clean_data(df)
    df = transform_data(df)
    return {
        'top_products': kpi_top_products(df),
        'revenue_by_category': kpi_revenue_by_category(df),
        'user_behavior': kpi_user_behavior(df),
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run analytics pipeline")
    parser.add_argument("--file", type=Path, default=Path("data/purchases.csv"))
    args = parser.parse_args()

    kpis = run_pipeline(args.file)
    print("Top products:\n", kpis['top_products'])
    print("\nRevenue by category:\n", kpis['revenue_by_category'])
    print("\nUser behavior:\n", kpis['user_behavior'])
