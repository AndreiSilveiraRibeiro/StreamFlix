# 🚀 Projeto Streamflix: Análise de Dados e Engenharia

Este projeto é um pipeline completo de dados, desde a limpeza e tratamento de uma base de assinantes (Streamflix) até a persistência em um banco de dados relacional (MySQL) para extração de insights de negócio.

# 🛠 Tecnologias Utilizadas

- **Linguagem:** Python

- **Manipulação:** Pandas, NumPy

- **Engenharia de Dados:** SQL (MySQL), SQLAlchemy, python-dotenv

- **Versionamento:** Git/GitHub

- **Ambiente:** VS Code

# 📊 Pipeline do Projeto

O fluxo de dados foi estruturado da seguinte forma:

- **Limpeza e Tratamento (limpeza_dados.py):** Padronização de datas, tratamento de valores nulos e correção de inconsistências na coluna de minutos assistidos.

- **Engenharia de Features (outliers_novo.py):** Detecção de outliers usando o método do Intervalo Interquartil (IQR), substituindo valores extremos pela mediana para evitar enviesamento na análise.

- **Persistência (carga_automatica.py):** Automação do envio dos dados tratados para um banco MySQL, utilizando variáveis de ambiente (.env) para garantir a segurança das credenciais.

- **Análise SQL (bdd.sql):** Consultas estruturadas para responder a perguntas de negócio.

# 🔍 Insights Obtidos

Através das consultas SQL, extraímos oportunidades estratégicas para a Streamflix:

- **Segmentação de Power Users:** Identificação de usuários com alto volume de minutos assistidos para campanhas de upgrade e retenção.

- **Análise de Engajamento por Plano:** Comparativo de consumo entre planos (Básico vs. Premium) para entender a preferência dos usuários.

- **Análise Temporal:** Mapeamento de tendências de adesão para otimizar campanhas de marketing em dias de maior conversão.

# 📂 Estrutura do Repositório

```
├── .env                 # Variáveis de ambiente (ignorado pelo Git)
├── .gitignore           # Arquivos excluídos do controle de versão
├── bdd.sql              # Consultas SQL para análise de dados
├── limpeza_dados.py     # Script de limpeza e pré-processamento
├── outliers_novo.py     # Script de detecção de outliers e carga no BD
└── Streamflix_limpo.csv # Base de dados final tratada
```

# 👨‍💻 Autor

**Andrei S.R**