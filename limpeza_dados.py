import pandas as pd
import numpy as np

# 1. Carregamento dos dados brutos
# Importa o arquivo CSV inicial para análise
tabela = pd.read_csv('streamflix_raw.csv')

# 2. Diagnóstico inicial do dataset
# Exibe a estrutura dos dados (linhas/colunas) e tipos de dados para identificar problemas
print(f"O DataFrame: \n{tabela}")
print(tabela.shape)
tabela.info()

# 3. Tratamento da coluna 'Data_Adesao'
# Verifica valores nulos antes da limpeza
print(tabela['Data_Adesao'])
print(f"Quantidade de valores nulos: {tabela['Data_Adesao'].isnull().sum()}")

# Padroniza diferentes formatos de data (/, .) para um formato único (-)
tabela['Data_Adesao'] = tabela['Data_Adesao'].str.replace("/", "-")
tabela['Data_Adesao'] = tabela['Data_Adesao'].str.replace(".", "-")
# Reorganiza a data de DD-MM-AAAA para AAAA-MM-DD (padrão ISO)
tabela['Data_Adesao'] = tabela['Data_Adesao'].str.replace(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\2-\1", regex=True)
# Converte a coluna para o tipo datetime do Pandas
tabela['Data_Adesao'] = pd.to_datetime(tabela['Data_Adesao'], errors='coerce')

# Verifica se a conversão gerou novos valores nulos (erros de formato)
print(f"Quantidade de valores nulos após conversão: {tabela['Data_Adesao'].isnull().sum()}")

# 4. Tratamento da coluna 'Minutos_Assistidos'
# Corrige valores negativos (transformando em positivos via valor absoluto)
# Assume que valores negativos foram erros de digitação
tabela['Minutos_Assistidos'] = np.where(tabela['Minutos_Assistidos'] < 0, tabela['Minutos_Assistidos'].abs(), tabela['Minutos_Assistidos'])

# Verifica se ainda restam valores negativos (esperado zero)
print(f"Valores negativos restantes: {(tabela['Minutos_Assistidos'] < 0).sum()}")
print(f"Total de valores nulos na coluna: {tabela['Minutos_Assistidos'].isnull().sum()}")

# 5. Tratamento da coluna 'Plano'
# Padroniza o texto: Capitaliza a primeira letra e remove acentuação em "Á" para garantir unicidade
tabela['Plano'] = tabela['Plano'].str.title()
tabela['Plano'] = tabela['Plano'].str.replace("á", "a")

# Exibe valores únicos para garantir que categorias como 'Basico' e 'Premium' estejam padronizadas
print(f"Categorias de plano após tratamento: {tabela['Plano'].unique()}")

# 6. Finalização e Exportação
# Verifica a integridade final dos dados antes de salvar
print(f"Resumo final do DataFrame: \n{tabela.shape}")
print(f"Valores nulos por coluna: \n{tabela.isnull().sum()}")

# Salva o arquivo tratado para ser utilizado no processo de carga ao banco de dados
tabela.to_csv('Streamflix_limpo.csv', index=False)

print('Arquivo limpo salvo com sucesso!')