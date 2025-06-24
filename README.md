# Analytics Pipeline

This repository contains a simple data analytics pipeline for a retail platform. It demonstrates how to ingest purchase data, clean and transform it, and produce key performance indicators (KPIs) such as top-selling products, revenue by category, and user behavior statistics.

## Requirements

- Python 3.8+
- `pandas`

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the pipeline with the sample data:

```bash
python -m analytics.analytics_pipeline --file data/purchases.csv
```

## Testing

A basic test script is provided:

```bash
python test_pipeline.py
```
