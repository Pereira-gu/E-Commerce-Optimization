import pandas as pd
from pathlib import Path

base = Path(__file__).parent.parent
df_orders = pd.read_csv(base / "data" / "raw" / "olist_orders_dataset.csv")
df_items = pd.read_csv(base / "data" / "raw" / "olist_order_items_dataset.csv")
df_customers = pd.read_csv(base / "data" / "raw" / "olist_customers_dataset.csv")

df_merge = pd.merge(df_orders, df_items, on="order_id")
df_merge = pd.merge(df_merge, df_customers, on="customer_id")
df_rfm = df_merge[df_merge["order_status"] == "delivered"].copy()
df_rfm["order_purchase_timestamp"] = pd.to_datetime(df_rfm["order_purchase_timestamp"])

snapshot_date = df_rfm["order_purchase_timestamp"].max() + pd.Timedelta(days=1)

print(f"Data de referência para o cálculo: {snapshot_date}")

rfm_final = (
    df_rfm.groupby("customer_unique_id")
    .agg(
        {
            "order_purchase_timestamp": lambda x: (snapshot_date - x.max()).days,
            "order_id": "nunique",
            "price": "sum",
        }
    )
    .reset_index()
)

rfm_final.columns = ["customer_id", "recencia", "frequencia", "valor"]
rfm_final["R"] = pd.qcut(rfm_final["recencia"], 5, labels=[5, 4, 3, 2, 1])
rfm_final["M"] = pd.qcut(rfm_final["valor"], 5, labels=[1, 2, 3, 4, 5])


def nota_frequencia(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    else:
        return 5


rfm_final["F"] = rfm_final["frequencia"].apply(nota_frequencia)
rfm_final["RFM_Score"] = (
    rfm_final["R"].astype(str) + rfm_final["F"].astype(str) + rfm_final["M"].astype(str)
)

segs = {
    r"[1-2][1-2]": "Perdidos",
    r"[1-2][3-4]": "Em Risco",
    r"[1-2]5": "Não podemos perder",
    r"3[1-2]": "Prestes a dormir",
    r"33": "Precisa de atenção",
    r"[3-4][4-5]": "Clientes Fiéis",
    r"41": "Promissores",
    r"51": "Novos Clientes",
    r"[4-5][2-3]": "Potenciais Fiéis",
    r"5[4-5]": "Campeões",
}

rfm_final["Segmento"] = rfm_final["R"].astype(str) + rfm_final["F"].astype(str)
rfm_final["Segmento"] = rfm_final["Segmento"].replace(segs, regex=True)

print("\n--- CLIENTES SEGMENTADOS ---")
print(rfm_final[["customer_id", "RFM_Score", "Segmento"]].head())

caminho_saida_rfm = base / "data" / "processed" / "df_rfm_final.csv"
rfm_final.to_csv(caminho_saida_rfm, index=False)
print(f"\nArquivo RFM salvo em: {caminho_saida_rfm}")
