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

faturamento_total = abc_base["price"].sum()
abc_base["percentual"] = (abc_base["price"] / faturamento_total) * 100
abc_base["percentual_acumulado"] = abc_base["percentual"].cumsum()


def categorizar_abc(acumulado):
    if acumulado <= 80:
        return "A"
    elif acumulado <= 95:
        return "B"
    else:
        return "C"


abc_base["categoria"] = abc_base["percentual_acumulado"].apply(categorizar_abc)
resumo_abc = (
    abc_base.groupby("categoria")
    .agg(
        quantidade_produtos=("product_id", "count"), faturamento_total=("price", "sum")
    )
    .reset_index()
)

resumo_abc["%_faturamento"] = (
    resumo_abc["faturamento_total"] / resumo_abc["faturamento_total"].sum()
) * 100

print("\n--- RESUMO ESTRATÉGICO DA CURVA ABC ---")
print(resumo_abc)

caminho_saida = base / "data" / "processed" / "df_curva_abc_final.csv"
caminho_saida.parent.mkdir(parents=True, exist_ok=True)

abc_base.to_csv(caminho_saida, index=False)
print(abc_base.head(20))
