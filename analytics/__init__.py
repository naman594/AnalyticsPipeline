"""Analytics pipeline package."""

from .analytics_pipeline import run_pipeline
from .ingestion import load_purchases
from .transformation import clean, add_revenue
from .kpis import top_products, revenue_by_category, user_behavior

__all__ = [
    "run_pipeline",
    "load_purchases",
    "clean",
    "add_revenue",
    "top_products",
    "revenue_by_category",
    "user_behavior",
]
