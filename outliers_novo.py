import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv

#Transformando o arquivo .csv em DataFrame
tabela = pd.read_csv('Streamflix_limpo.csv')

load_dotenv()

usuario = os.getenv('DB_USER')
senha = os.getenv('DB_PASS')
host = '127.0.0.1'
db = 'Streamflix'

print(tabela.describe())
print(tabela['Minutos_Assistidos'].sort_values(ascending=False))

Q1 = tabela['Minutos_Assistidos'].quantile(0.25)
Q3 = tabela['Minutos_Assistidos'].quantile(0.75)
IQR =   Q3 - Q1

limite_alto = Q3 + (1.5 * IQR)
limite_baixo = Q1 - (1.5 * IQR)

outliers = tabela[(tabela['Minutos_Assistidos'] < limite_baixo) | (tabela['Minutos_Assistidos'] > limite_alto)]

print(f"Oportunidade para aumentar o plano para por tempo indeterminado e dar desconto na primeira assinatura: \n{tabela[tabela['Minutos_Assistidos'] > limite_alto]}")

print(f"Usuarios que deve prestar atenção e tentar aumentar o tempo assistido: \n{tabela[tabela['Minutos_Assistidos'] < limite_baixo]}")

media = tabela['Minutos_Assistidos'].median()

tabela['Minutos_Assistidos'] = np.where(tabela['Minutos_Assistidos'] > limite_alto, media, tabela['Minutos_Assistidos'])

print(outliers)
print(tabela[(tabela['Minutos_Assistidos'] < limite_baixo) | (tabela['Minutos_Assistidos'] > limite_alto)])

engine = create_engine(f'mysql+mysqlconnector://{usuario}:{senha}@{host}/{db}')

outliers.to_csv("Outliers.csv", index=False)
tabela.to_csv("tabela_dashboard.csv", index=False)
tabela.to_sql('usuarios', con=engine, if_exists='replace', index=False)