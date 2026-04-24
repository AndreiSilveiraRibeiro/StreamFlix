import pandas as pd
import numpy as np

#Transformando o arquivo .csv em DataFrame
leitura = pd.read_csv('streamflix_raw.csv')

#Analisando o DataFrame para ver possiveis correções
print(f"O DataFrame: \n{leitura}")

#Verificando se os tipos das colunas estão certos
print(f"Os tipos de cada coluna do DataFrame:")
leitura.info()

#Analisando a quantidade de linha que tem no inicio para verificar no final
print(f"Quantidade de linha e coluna: {leitura.shape}")

#Analisando especificamente a coluna 'Data_Adesao' para ver oque tem de errado e possiveis melhoras
print(f"Coluna 'Data_Adesao' original: \n{leitura['Data_Adesao']}")

#Transfomardo a coluna 'Data_Adesao' em DataTime
leitura['Data_Adesao'] = pd.to_datetime(leitura['Data_Adesao'], format='mixed', dayfirst=True, errors='coerce')

#Verificando se sobrou algo para fazer na coluna e se está tudo certo
print(f"Correção da coluna 'Data_Adesao': \n{leitura['Data_Adesao']}")

#Analisando se tem numeros negativos na coluna 'Minutos_Assistidos'
print(leitura[leitura['Minutos_Assistidos'] <= 0])

#Se tiver coloquei para ser retirado
leitura['Minutos_Assistidos'] = leitura['Minutos_Assistidos'].mask(leitura['Minutos_Assistidos'] < 0, 0)

#Verificando se está tudo certo
print(leitura[leitura['Minutos_Assistidos'] <= 0])

#Analisando agora a coluna 'Plano'
print(leitura['Plano'])

#Arrumando e deixando tudo padronizado
leitura['Plano'] = leitura['Plano'].str.title()
#Troca de acento para sem
leitura['Plano'] = leitura['Plano'].replace('Básico', 'Basico')

#Verificando se deu certo
print(leitura['Plano'])

#Tirando duplicatas e apagando dados nulos
leitura.drop_duplicates()
leitura = leitura.dropna()

#Verificando se tem dados nulos, quantas colunas foram perdidas e como ta o DataFrame
print(leitura.isnull().sum())
print(leitura.shape)
print(leitura)

#Salvando o DataFrame como .csv
leitura.to_csv('Streamflix_limpo.csv', index=False)

#Retorno para verificar se deu certo
print('Salvo com sucesso!')