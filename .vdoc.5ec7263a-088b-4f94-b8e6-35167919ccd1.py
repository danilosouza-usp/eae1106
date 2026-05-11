# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| message: false
#| warning: false

import numpy as np
import pandas as pd
import os
#
#
#
#| echo: false
from IPython.display import display, HTML

display(HTML("""
<style>
table.dataframe td {
    text-align: center;
}
table.dataframe th {
    text-align: center;
}
</style>
"""))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
pessoas_ocupadas = [90593,92170,92962,92366,90174,92228,93534,95515,87225,95747]
anos = list(range(2012,2021+1))

print(pessoas_ocupadas)
print(anos)
#
#
#
#
#
series_pessoas_ocup = pd.Series(data=pessoas_ocupadas,index=anos)

print(type(series_pessoas_ocup),'\n')
print(series_pessoas_ocup)
#
#
#
#
#
dados = {
    'ocupadas': [90593,92170,92962,92366,90174,92228,93534,95515,87225,95747],
    'desocupadas': [6730,6151,6555,9222,12476,12453,12413,11903,14412,12011],
    'na forca': [97322,98321,99516,101588,102650,104682,105947,107418,101637,107758],
    'fora da forca': [58007,59244,60162,60092,60953,60777,61299,61579,69042,64525]
}

print(dados)
#
#
#
#
#
dados_emprego = pd.DataFrame(data=dados,index=anos)

print(type(dados_emprego),'\n')
dados_emprego.head()
#
#
#
#
#
#
#
#
#
#
#
#| echo: false
os.chdir('D:/Dropbox')
#
#
#
# Qual o diretório no qual o Python está trabalhando? A função getcwd() nos diz isso
print('Diretório inicial: {}'.format(os.getcwd()))

# Vamos mudar para o nosso diretório atual
os.chdir('C:/Users/user/Desktop/EAE1106')
print('Diretório final: {}'.format(os.getcwd()))
#
#
#
#
#
os.listdir()
#
#
#
#
#
df_pwt = pd.read_csv('pwt110_selected.csv', sep=';', encoding='utf8')
type(df_pwt)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
df_pwt.info(memory_usage='deep')
#
#
#
df_pwt.head(2) # método para apresentar apenas as primeiras duas linhas do dataframe
#
#
#
#
#
pd.set_option('display.max_columns', 100)
df_pwt.head(2)
#
#
#
df_pwt.describe()
#
#
#
#
#
df_pwt['country'].value_counts()
#
#
#
#
#
df_pwt['country'].value_counts(normalize=True,dropna=False)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
df_pwt[0:2]
#
#
#
#
#
df_pwt.iloc[:,1:7]
#
#
#
#
#
columns_to_keep = ['country','currency_unit','year','pop','emp','rgdpna']

df_pwt.loc[:, columns_to_keep]
#
#
#
#
#
df_pwt2 = df_pwt[columns_to_keep]

df_pwt2.head()
#
#
#
#
#
df_pwt2.columns = ['pais','moeda','ano','populacao (milhoes)','pessoas empregadas (milhoes)','PIB real em valores de 2021 (milhoes US$)']
df_pwt2.head()
#
#
#
#
#
#
#
cond1 = df_pwt2['pais']=='Brazil'

df_pwt2[cond1].head()
#
#
#
#
#
cond2 = df_pwt2['ano']>=2000

df_pwt2[(cond1) & (cond2)].head()
#
#
#
#
#
cond1 = df_pwt2['pais'].isin(['Brazil','United States'])

df_pwt2[cond1].head()
#
#
#
#
#
#
#
# O método reset_index nesse caso, serve para renumerar as linhas a partir do zero.
df_pwtbr = df_pwt2[df_pwt2['pais']=='Brazil'].reset_index()

df_pwtbr.head()
#
#
#
#
#
df_pwtbr['pibpc'] = df_pwtbr['PIB real em valores de 2021 (milhoes US$)'] / df_pwtbr['populacao (milhoes)']

columns_to_show = ['ano','populacao (milhoes)','PIB real em valores de 2021 (milhoes US$)','pibpc']
df_pwtbr[columns_to_show].head()
#
#
#
#
#
df_pwtbr['log_pibpc'] = np.log(df_pwtbr['pibpc'])

columns_to_show = ['ano','pibpc','log_pibpc']
df_pwtbr[columns_to_show].head()
#
#
#
#
#
df_pwtbr['pibpc_th'] = df_pwtbr['pibpc'] / 1000

columns_to_show = ['ano','pibpc','pibpc_th']
df_pwtbr[columns_to_show].head()
#
#
#
#
#
df_pwtbr['r_emppop'] = df_pwtbr['pessoas empregadas (milhoes)'] / df_pwtbr['populacao (milhoes)']
df_pwtbr['r_emppop'] = df_pwtbr['r_emppop'] - df_pwtbr['r_emppop'].mean()

columns_to_show = ['ano','r_emppop','r_emppop']
df_pwtbr[columns_to_show].head()
#
#
#
#
#
#
#
df_pwtbr['pop_sqrt'] = df_pwtbr['populacao (milhoes)'].apply(lambda x: ((x*1000000)**0.5))

columns_to_show = ['ano','populacao (milhoes)','pop_sqrt']
df_pwtbr[columns_to_show].head()
#
#
#
#
#
print(df_pwtbr.loc[10,'populacao (milhoes)'])
print(df_pwtbr.loc[10,'pop_sqrt'])
print((df_pwtbr.loc[10,'populacao (milhoes)'] * 1000000)**0.5)
#
#
#
#
#
#
#
#
#
df_pwtbr['lower_pais'] = df_pwtbr['pais'].str.lower()

columns_to_show = ['pais','lower_pais','ano']
df_pwtbr[columns_to_show].head()
#
#
#
#
#
#
#
df_pwtbr['r_emppop'].describe()
#
#
#
# criando coluna a partir de list comprehension
df_pwtbr['remppop_p75bool'] = [True if x>=100 else False for x in df_pwtbr['r_emppop']]

# criando coluna a partir de um dicionario
quartil_sup = {
    True:'Acima do 3º quartil',
    False:'Abaixo do 3º quartil'}

df_pwtbr['remppop_p75cat'] = df_pwtbr['remppop_p75bool'].apply(lambda x: quartil_sup[x])
#
#
#
#
#
columns_to_show = ['ano','r_emppop','remppop_p75bool','remppop_p75cat']
df_pwtbr[columns_to_show].head()
#
#
#
#
#
#
#
df_pwt2['decada'] = np.trunc(df_pwt2['ano']/10) * 10
df_pwt2['pibpc'] = df_pwt2['PIB real em valores de 2021 (milhoes US$)'] / df_pwt2['populacao (milhoes)']
df_pwt2['r_emppop'] = df_pwt2['pessoas empregadas (milhoes)'] / df_pwt2['populacao (milhoes)']

columns_to_keep = ['pais','decada','pibpc','r_emppop']

df_pwtdbr = df_pwt2.loc[df_pwt2['pais']=='Brazil', columns_to_keep]
df_pwtdus = df_pwt2.loc[df_pwt2['pais']=='United States', columns_to_keep]

df_pwtdbr.head(2)
#
#
#
#
#
df_pwtdbr = df_pwtdbr.groupby(by=['pais','decada']).mean()
df_pwtdbr.head(5)
#
#
#
df_pwtdus = df_pwtdus.groupby(by=['pais','decada'], as_index=False).mean()
df_pwtdus.head(5)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
df_pwt_concat = pd.concat(objs=[df_pwtdbr, df_pwtdus]).reset_index(drop=True)

df_pwt_concat
#
#
#
#
#
#
#
#
#
df_pwt_merge = pd.merge(df_pwtdbr, df_pwtdus, how='inner', on=['decada'])

df_pwt_merge
#
#
#
#
#
dict_rename = {
    'pibpc_x':'pibpc_br',
    'r_emppop_x':'r_emppop_br',
    'pibpc_y':'pibpc_us',
    'r_emppop_y':'r_emppop_us'}

df_pwt_merge.rename(columns=dict_rename, inplace=True)

df_pwt_merge.head()
#
#
#
#
#
#
#
#
#
#
#
#
df_pwt_merge.to_csv('df_resultado_aula_pandas.csv', sep=',', encoding='utf8', index=False)

os.listdir()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
