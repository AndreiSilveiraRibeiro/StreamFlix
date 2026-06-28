import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Carregamento e Preparação
# Carrega o arquivo limpo gerado anteriormente
tabela = pd.read_csv('Streamflix_limpo.csv')

# Carrega as credenciais de segurança do arquivo .env
load_dotenv()
usuario = os.getenv('DB_USER')
senha = os.getenv('DB_PASS')
host = '127.0.0.1'
db = 'Streamflix'

# 2. Análise Estatística Preliminar
# Exibe resumo estatístico e ordena os minutos assistidos para visualização
print(tabela.describe())
print(tabela['Minutos_Assistidos'].sort_values(ascending=False))

# 3. Detecção de Outliers via Método IQR (Intervalo Interquartil)
# Calcula os limites para identificar comportamentos fora do padrão (muito acima ou muito abaixo)
Q1 = tabela['Minutos_Assistidos'].quantile(0.25)
Q3 = tabela['Minutos_Assistidos'].quantile(0.75)
IQR = Q3 - Q1

limite_alto = Q3 + (1.5 * IQR)
limite_baixo = Q1 - (1.5 * IQR)

# Filtra e armazena os registros que estão fora dos limites calculados
outliers = tabela[(tabela['Minutos_Assistidos'] < limite_baixo) | (tabela['Minutos_Assistidos'] > limite_alto)]

# Imprime os insights de negócio baseados nos outliers
print(f"Oportunidade para aumentar o plano: \n{tabela[tabela['Minutos_Assistidos'] > limite_alto]}")
print(f"Usuarios que devem receber atenção (baixo engajamento): \n{tabela[tabela['Minutos_Assistidos'] < limite_baixo]}")

# 4. Tratamento de Dados (Limpeza de Outliers)
# Substitui valores extremos superiores pela mediana para suavizar a análise
media = tabela['Minutos_Assistidos'].median()
tabela['Minutos_Assistidos'] = np.where(tabela['Minutos_Assistidos'] > limite_alto, media, tabela['Minutos_Assistidos'])

# Validação do tratamento realizado
print(outliers)
print(tabela[(tabela['Minutos_Assistidos'] < limite_baixo) | (tabela['Minutos_Assistidos'] > limite_alto)])

# 5. Carga de Dados e Persistência
# Cria a conexão com o banco MySQL
engine = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{db}')

# Exporta resultados para arquivos CSV para backup/dashboard
outliers.to_csv("Outliers.csv", index=False)
tabela.to_csv("tabela_dashboard.csv", index=False)

# Envia a tabela tratada para o MySQL (cria/substitui a tabela 'usuarios')
tabela.to_sql('usuarios', con=engine, if_exists='replace', index=False) 

print("Pipeline finalizado: Dados tratados, exportados e carregados no MySQL com sucesso!"