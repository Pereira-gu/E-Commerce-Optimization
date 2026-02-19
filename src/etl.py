"""Entry point for data processing pipeline."""

from src import data_loader
import pandas as pd


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic cleaning on orders table."""
    # convert timestamps
    ts_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    for col in ts_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # drop rows without key identifiers
    df = df.dropna(subset=["order_id", "customer_id"])

    return df


def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning for customers."""
    # nothing special for now
    return df.dropna(subset=['customer_id'])


def clean_order_items(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=['order_id', 'product_id'])
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['freight_value'] = pd.to_numeric(df['freight_value'], errors='coerce')
    return df


def run():
    # load raw tables
    tables = data_loader.load_all_tables()

    # orders
    if 'olist_orders_dataset' in tables:
        orders = tables['olist_orders_dataset']
        orders = clean_orders(orders)
        data_loader.save_processed(orders, 'orders')

    # customers
    if 'olist_customers_dataset' in tables:
        customers = tables['olist_customers_dataset']
        customers = clean_customers(customers)
        data_loader.save_processed(customers, 'customers')

    # order items
    if 'olist_order_items_dataset' in tables:
        order_items = tables['olist_order_items_dataset']
        order_items = clean_order_items(order_items)
        data_loader.save_processed(order_items, 'order_items')

    # additional cleaning steps can be appended similarly


if __name__ == "__main__":
    run()
