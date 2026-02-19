"""Utilities for loading and saving project data."""

from pathlib import Path
import pandas as pd

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
PROCESSED_DIR = Path(__file__).parent.parent / "data" / "processed"


def load_csv(name: str, **kwargs) -> pd.DataFrame:
    """Load a CSV file from the raw directory.

    Parameters
    ----------
    name : str
        Filename of the CSV (with or without .csv extension).
    kwargs : dict
        Forwarded to :func:`pandas.read_csv`.
    """
    path = RAW_DIR / (name if name.lower().endswith(".csv") else name + ".csv")
    return pd.read_csv(path, **kwargs)


def load_all_tables() -> dict[str, pd.DataFrame]:
    """Read every CSV file found under ``data/raw`` and return a dict."""
    tables: dict[str, pd.DataFrame] = {}
    for csv_path in RAW_DIR.glob("*.csv"):
        key = csv_path.stem
        tables[key] = pd.read_csv(csv_path)
    return tables


def save_processed(df: pd.DataFrame, name: str, **kwargs) -> None:
    """Write a DataFrame to the processed directory as parquet.

    Parameters mirror :func:`pandas.DataFrame.to_parquet`.
    """
    PROCESSED_DIR.mkdir(exist_ok=True)
    outfile = PROCESSED_DIR / f"{name}.parquet"
    df.to_parquet(outfile, **kwargs)
