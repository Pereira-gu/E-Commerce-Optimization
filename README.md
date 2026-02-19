📊 E-Commerce Analytics Pro: Otimização de Estoque e Clientes
Este projeto de Ciência de Dados foca na extração de inteligência estratégica a partir de dados reais de e-commerce (Dataset Olist). A solução une o poder de processamento do Python com a clareza visual do Power BI para resolver dois problemas críticos: a gestão eficiente de estoque e a fidelização de clientes.


🚀 Tecnologias Utilizadas
Linguagem: Python 3.x

Manipulação de Dados: Pandas, Numpy

Processamento de Caminhos: Pathlib (Cross-platform)

Visualização: Power BI Desktop

Dataset: Olist E-commerce Public Dataset

🛠️ O que o projeto resolve?
1. Análise de Pareto (Curva ABC)
Utilizei a regra dos 80/20 para identificar quais produtos sustentam o faturamento do negócio.

Lógica: Agrupamento por faturamento acumulado e classificação em categorias (A, B, C).

Impacto: Permite que o gestor foque esforços de estoque nos itens da Classe A, evitando rupturas em produtos essenciais e reduzindo custos em itens de baixa rotatividade (Classe C).

2. Segmentação RFM (Recência, Frequência, Valor)
Uma análise profunda do comportamento do consumidor para classificar a base de clientes.

Lógica: Cálculo de scores (1-5) para identificar a última compra, a frequência de pedidos e o gasto total.

Categorias: Criação de segmentos automáticos como "Campeões", "Clientes Fiéis", "Em Risco" e "Novos Clientes".

📈 Dashboard Estratégico
O dashboard foi desenvolvido com foco em UX (User Experience), utilizando um design minimalista e intuitivo para facilitar a tomada de decisão:

KPIs de Topo: Visão instantânea de Faturamento Total, Mix de Produtos e Ticket Médio.

Interatividade: Filtros por categoria ABC que permitem o detalhamento da performance de cada grupo.

Visual Pareto: Gráfico de colunas e linha para visualização clara da concentração de receita.

📂 Estrutura do Repositório
Plaintext
├── data/
│   ├── raw/         # Dados brutos originais
│   └── processed/   # Dados limpos e prontos para o BI
├── notebooks/       # Scripts Python para processamento
└── dashboards/      # Arquivos do Power BI (.pbix)
🧠 Como Rodar
Certifique-se de ter os dados na pasta data/raw/.

Execute os scripts na pasta notebooks/ para gerar os arquivos processados.

Abra o arquivo do Power BI e atualize a fonte de dados para data/processed/.