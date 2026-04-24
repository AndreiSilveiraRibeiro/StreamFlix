import pandas as pd
import numpy as np
from scipy import stats

leitura = pd.read_csv('Streamflix_limpo.csv')

leitura['z_score'] = np.abs(stats.zscore(leitura['Minutos_Assistidos']))

outliers = leitura[leitura['Minutos_Assistidos'] > 3]

print(f"Possiveis oportunidades: {len(outliers)}")