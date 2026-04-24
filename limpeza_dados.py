import pandas as pd
import numpy as np

leitura = pd.read_csv('streamflix_raw.csv')

print(f"O DataFrame: \n{leitura}")

print(f"Os tipos de cada coluna do DataFrame:")
leitura.info()

print(f"Quantidade de linha e coluna: {leitura.shape}")

print(f"Coluna 'Data_Adesao' original: \n{leitura['Data_Adesao']}")

leitura['Data_Adesao'] = pd.to_datetime(leitura['Data_Adesao'], format='mixed', dayfirst=True, errors='coerce')

print(f"Correção da coluna 'Data_Adesao': \n{leitura['Data_Adesao']}")

print(leitura[leitura['Minutos_Assistidos'] <= 0])

leitura['Minutos_Assistidos'] = leitura['Minutos_Assistidos'].apply(lambda x: x if x >= 0 else 0)

print(leitura[leitura['Minutos_Assistidos'] <= 0])

print(leitura['Plano'])

leitura['Plano'] = leitura['Plano'].str.title()

print(leitura['Plano'])

leitura.drop_duplicates()
leitura = leitura.dropna()

print(leitura.isnull().sum())
print(leitura.shape)
print(leitura)

leitura.to_csv('Streamflix_limpo.csv')

print('Salvo com sucesso!')