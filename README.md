📊 E-Commerce Optimization - Inteligência de Dados com Python & Power BI

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Status](https://img.shields.io/badge/status-completo-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%26%20Unix-lightgrey.svg)

> Atenção: Este é um projeto de portfólio desenvolvido para demonstrar competências avançadas em Data Analytics e Data Engineering. O objetivo é transformar dados brutos de e-commerce em decisões estratégicas de negócio.

🔗 [Repositório GitHub](https://github.com/Pereira-gu/E-Commerce-Optimization)

� Índice
- [Sobre](#sobre-o-projeto)
- [Funcionalidades](#-principais-funcionalidades)
- [Tecnologias](#-tecnologias-utilizadas)
- [Requisitos](#-requisitos-mínimos)
- [Como Executar](#-como-executar-localmente)
- [Estrutura](#-estrutura-de-pastas)
- [Dataset](#-dataset)
- [Troubleshooting](#-troubleshooting)
- [Autor](#-autor)

---

�📖 Sobre o Projeto
O E-Commerce Optimization é uma solução de análise de dados de ponta a ponta que utiliza o dataset público da Olist para otimizar operações logísticas e estratégias de marketing. O projeto resolve dois desafios reais do setor: identificar a relevância do inventário (Curva ABC) e mapear o comportamento e fidelidade dos consumidores (Segmentação RFM).

Ao contrário de análises superficiais, este projeto foca na limpeza rigorosa dos dados e no cálculo de métricas complexas via Python, entregando um painel executivo visualmente limpo e funcional no Power BI.

✨ Principais Funcionalidades
🛒 Análise de Pareto (Curva ABC)
Identificação de Ativos Críticos: Agrupamento de mais de 100 mil pedidos para identificar os produtos "Classe A" que sustentam o faturamento.

Cálculo de Faturamento Acumulado: Lógica implementada em Python para calcular o percentual de representatividade de cada SKU.

Gestão de Inventário: Classificação automática em categorias A, B e C para auxiliar na tomada de decisão de estoque.

👥 Segmentação de Clientes (RFM)
Recência: Cálculo de dias desde a última compra por cliente único.

Frequência: Identificação da recorrência de compras na plataforma.

Valor Monetário: Análise do gasto total acumulado por utilizador.

Scores Comportamentais: Atribuição de notas de 1 a 5 para segmentar clientes em grupos como "Campeões", "Em Risco" ou "Novos Clientes".

📈 Dashboard Executivo (Power BI)
Design Minimalista: Interface clean focada na experiência do utilizador (UX).

KPIs em Tempo Real: Visualização instantânea de Faturamento Total, Mix de Produtos e Ticket Médio.

Filtros Dinâmicos: Segmentação interativa por categorias ABC para análise detalhada.

🚀 Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| **Python** | 3.11+ | Linguagem principal com foco em performance |
| **Pandas** | 2.x | Manipulação e análise de dados |
| **NumPy** | 1.x | Operações numéricas vetorizadas |
| **PyArrow** | 14.x | Serialização Parquet para performance |
| **SciPy** | 1.x | Cálculos estatísticos |
| **Power BI** | 2.x | Dashboard executivo e visualizações |
| **pathlib** | built-in | Compatibilidade cross-platform |

**Dataset:** Olist E-commerce Public Dataset (Kaggle)

⚙️ Requisitos Mínimos

- **Python:** 3.9 ou superior
- **RAM:** 4GB recomendado (2GB mínimo)
- **Espaço em Disco:** ~2GB para dataset + venv
- **Tempo de Execução:** ~5-10 minutos para processar todo o dataset
- **Power BI:** Versão 2.x Desktop (para visualizar dashboard)

---

🔧 Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/Pereira-gu/E-Commerce-Optimization.git
cd E-Commerce-Optimization
```

### 2. Configure o Ambiente Virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux (Bash):**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Organize os Dados

Certifique-se de que os ficheiros `.csv` originais da Olist estão em:
```
data/raw/
├── olist_customers_dataset.csv
├── olist_orders_dataset.csv
├── olist_order_items_dataset.csv
├── olist_products_dataset.csv
├── olist_sellers_dataset.csv
└── ...
```

### 5. Execute os Scripts de Processamento

```bash
# Processa Curva ABC
python notebooks/processamento_abc.py

# Processa Segmentação RFM
python notebooks/processamento_rfm.py
```

**Saída esperada:**
```
data/processed/
├── df_curva_abc_final.csv
└── df_rfm_final.csv
```

### 6. Visualize o Dashboard

1. Abra o ficheiro `PowerBi/Painel de Otimização Logistica.pbix`
2. No Power BI, atualize a fonte de dados:
   - Clique em "Transformar dados" → "Fontes de dados"
   - Aponte para os ficheiros em `data/processed/`
3. Atualize os gráficos com o atalho `Ctrl+R`

� Dataset

**Fonte:** [Olist E-commerce Dataset - Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Características:**
- **Período:** 2016 - 2018
- **Registros:** ~100k pedidos
- **Dimensões:** ~8 ficheiros CSV interligados
- **Tamanho Total:** ~70MB (dados brutos)
- **Cobertura Geográfica:** Brasil inteiro

**Tabelas Principais:**
- `olist_orders_dataset.csv` — Pedidos e datas
- `olist_order_items_dataset.csv` — Itens por pedido
- `olist_customers_dataset.csv` — Informações de clientes
- `olist_products_dataset.csv` — Catálogo de produtos
- `olist_sellers_dataset.csv` — Informações de vendedores

---

📂 Estrutura de Pastas

```
E-Commerce-Optimization/
├── data/
│   ├── raw/               # Dados originais da Olist (não versionados)
│   └── processed/         # Dados limpos (CSV/Parquet)
├── notebooks/             # Scripts Python de processamento
│   ├── processamento_abc.py
│   └── processamento_rfm.py
├── src/                   # Módulos reutilizáveis
│   ├── data_loader.py
│   ├── etl.py
│   └── __init__.py
├── PowerBi/               # Dashboard executivo
│   └── Painel de Otimização Logistica.pbix
├── README.md              # Este ficheiro
├── requirements.txt       # Dependências Python
└── .gitignore             # Ficheiros ignorados por Git
```

❓ Troubleshooting

| Problema | Causa | Solução |
|----------|-------|----------|
| `ModuleNotFoundError: pandas` | Dependências não instaladas | Execute `pip install -r requirements.txt` |
| `FileNotFoundError: data/raw/` | Dados não estão no lugar | Copie os CSV originais para `data/raw/` |
| Power BI não encontra dados | Path relativo incorreto | Use caminho absoluto ou reabra o ficheiro .pbix |
| Script faz timeout | Dataset grande | Aumente o tempo ou processe por chunck |
| Erro de encoding UTF-8 | Ficheiros com caracteres especiais | Use `encoding='utf-8'` no pandas |

---

📄 Licença

MIT License — Veja `LICENSE` para detalhes.

---

👤 Autor

**Gustavo Pereira**

- GitHub: [@Pereira-gu](https://github.com/Pereira-gu)
- LinkedIn: [Gustavo dos Santos Pereira](https://linkedin.com/in/gustavo-pereira-ds)

---

⭐ Se este projeto foi útil, considere dar uma estrela no GitHub!