import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent  # dois níveis acima (raiz)
itens = pd.read_csv(base / "data" / "raw" / "olist_order_items_dataset.csv")
pedidos = pd.read_csv(base / "data" / "raw" / "olist_orders_dataset.csv")

df_completo = pd.merge(itens, pedidos, on="order_id", how="left")
df_limpo = df_completo[df_completo["order_status"] == "delivered"].copy()
df_abc = df_limpo[["product_id", "price"]]
abc_base = df_abc.groupby("product_id")["price"].sum().reset_index()
abc_base = abc_base.sort_values(by="price", ascending=False)

print(abc_base.head(10))
