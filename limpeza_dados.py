import pandas as pd
import numpy as np

#Transformando o arquivo .csv em DataFrame
tabela = pd.read_csv('streamflix_raw.csv')

#Analisando o DataFrame para ver possiveis correções
print(f"O DataFrame: \n{tabela}")
print(tabela.shape)
tabela.info()

print(tabela['Data_Adesao'])
print(f"Quantidade de valores nulos: {tabela['Data_Adesao'].isnull().sum()}")

tabela['Data_Adesao'] = tabela['Data_Adesao'].str.replace("/", "-")
tabela['Data_Adesao'] = tabela['Data_Adesao'].str.replace(".", "-")
tabela['Data_Adesao'] = tabela['Data_Adesao'].str.replace(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\2-\1", regex=True)
tabela['Data_Adesao'] = pd.to_datetime(tabela['Data_Adesao'], errors='coerce')

print(f"Quantidade de valores nulos: {tabela['Data_Adesao'].isnull().sum()}")
print(tabela['Data_Adesao'])

print(tabela['Minutos_Assistidos'])

print(tabela[tabela['Minutos_Assistidos'] < 0])
print(tabela[tabela['Plano'] == 'premium'])

tabela['Minutos_Assistidos'] = np.where(tabela['Minutos_Assistidos'] < 0, tabela['Minutos_Assistidos'].abs(), tabela['Minutos_Assistidos'])

print(tabela[tabela['Minutos_Assistidos'] < 0])
print(tabela[tabela['Plano'] == 'premium'])
print(tabela['Minutos_Assistidos'].isnull().sum())

print(tabela['Plano'])
print(tabela['Plano'].isnull().sum())
print(tabela['Plano'].unique())

tabela['Plano'] = tabela['Plano'].str.title()
tabela['Plano'] = tabela['Plano'].str.replace("á", "a")

print(tabela['Plano'])
print(tabela['Plano'].unique())

print(f"O DataFrame: \n{tabela}")
print(tabela.shape)
tabela.info()
print(tabela.isnull().sum())

tabela.to_csv('Streamflix_limpo.csv', index=False)

#Retorno para verificar se deu certo
print('Salvo com sucesso!')