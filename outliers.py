import pandas as pd
import numpy as np
from scipy import stats

#Transformando o arquivo .csv em DataFrame
leitura = pd.read_csv('Streamflix_limpo.csv')

#Criando uma coluna chamada 'z_score' para colocar todos os novos dados 
leitura['z_score'] = np.abs(stats.zscore(leitura['Minutos_Assistidos']))

#Analisando se tem outliers 
outliers = leitura[leitura['z_score'] > 3]

#Verificando as possiveis oportunidades de fazer alguma coisa sobre
print(f"Possiveis oportunidades: {len(outliers)}")

#Verificando se está tudo certo
print(leitura)