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
#| message: false
#| warning: false

import numpy as np
import pandas as pd
import os
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
dados_emprego
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
import os

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
df_pwt = pd.read_csv('pwt110_selected.csv', sep=',', encoding='utf8')
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
df_pwt[0:2]
#
#
#
#
#
#| error: true
df_pwt[0:2,2]
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
#
df_pwt2 = df_pwt[columns_to_keep]

df_pwt2.head(2)
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

df_pwt2[cond1]
#
#
#
#
#
cond2 = df_pwt2['ano']>=2000

df_pwt2[(cond1) & (cond2)]
#
#
#
#
#
cond1 = df_pwt2['pais'].isin(['Brazil','United States'])

df_pwt2[cond1]
#
#
#
#
#
#
#
df_pwtbr = df_pwt2[df_pwt2['pais']=='Brazil'].reset_index()

df_pwtbr.head(2)
#
#
#
#
#
df_pwtbr['pibpc'] = df_pwtbr['PIB real em valores de 2021 (milhoes US$)'] / df_pwtbr['populacao (milhoes)']

columns_to_show = ['ano','populacao (milhoes)','PIB real em valores de 2021 (milhoes US$)','pibpc']
df_pwtbr[columns_to_show]
#
#
#
#
#
df_pwtbr['log_pibpc'] = np.log(df_pwtbr['pibpc'])

columns_to_show = ['ano','pibpc','log_pibpc']
df_pwtbr[columns_to_show]
#
#
#
#
#
df_pwtbr['pibpc_th'] = df_pwtbr['pibpc'] / 1000

columns_to_show = ['ano','pibpc','pibpc_th']
df_pwtbr[columns_to_show]
#
#
#
#
#
df_pwtbr['r_emppop'] = df_pwtbr['pessoas empregadas (milhoes)'] / df_pwtbr['populacao (milhoes)']
df_pwtbr['r_emppop'] = df_pwtbr['r_emppop'] - df_pwtbr['r_emppop'].mean()

columns_to_show = ['ano','r_emppop','r_emppop']
df_pwtbr[columns_to_show]
#
#
#
#
#
#
#
df_pwtbr['pop_sqrt'] = df_pwtbr['populacao (milhoes)'].apply(lambda x: ((x*1000000)**0.5))

columns_to_show = ['ano','pop','pop_sqrt']
df_pwtbr[columns_to_show]
#
#
#
#
#
print(df_covid_br.loc[100,'populacao (milhoes)'])
print(df_covid_br.loc[100,'pop_sqrt'])
print((df_covid_br.loc[100,'populacao (milhoes)'] * 1000000)**0.5)
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
df_covid_br['lower_location'] = df_covid_br['location'].str.lower()

columns_to_show = ['iso_code','continent','location','lower_location','date']
df_covid_br[columns_to_show]
#
#
#
#
#
#
df_covid_br[['continent_1', 'continent_2']] = df_covid_br['continent'].str.split(pat=' ',n=1, expand=True, regex=False)

columns_to_show = ['iso_code','continent','continent_1','continent_2','location','lower_location','date']
df_covid_br[columns_to_show]
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
df_covid_br['new_cases_per_million'].describe()
#
#
#
#
# criando coluna a partir de list comprehension
df_covid_br['quartil_superior_bool'] = [True if elem>=254.279 else False for elem in df_covid_br['new_cases_per_million']]


# criando coluna a partir de um dicionario
quartil_superior = {
    True:'Acima do 3º quartil de novos casos por milhão',
    False:'Abaixo'
}

df_covid_br['quartil_superior_cat'] = df_covid_br['quartil_superior_bool'].apply(lambda x: quartil_superior[x])
#
#
#
#
#
#
df_covid_br[['date','new_cases_per_million','quartil_superior_bool','quartil_superior_cat']]
#
#
#
#
#
#
#
#
#
df_covid['ano_mes'] = df_covid['date'].str[0:7]
columns_to_keep = ['location','ano_mes','new_cases','new_cases_per_million']

df_covid_br = df_covid[df_covid['iso_code']=='BRA'][columns_to_keep]
df_covid_us = df_covid[df_covid['iso_code']=='USA'][columns_to_keep]

df_covid_br.head(2)
#
#
#
#
df_covid_br_mensal = df_covid_br.groupby(by=['location','ano_mes'], as_index=False).mean()
df_covid_us_mensal = df_covid_us.groupby(by=['location','ano_mes'], as_index=False).mean()

df_covid_br_mensal
#
#
#
#
#
#
#
#
df_covid_concat = pd.concat(objs=[df_covid_br_mensal, df_covid_us_mensal]).reset_index(drop=True)

df_covid_concat
#
#
#
#
#
#
df_covid_merge = pd.merge(df_covid_br_mensal, df_covid_us_mensal, how='inner', on=['ano_mes'])

df_covid_merge
#
#
#
#
#
#
#
#
df_covid_merge.drop(columns=['location_x','location_y'], inplace=True)

dict_rename = {
    'new_cases_x':'nc_br',
    'new_cases_per_million_x':'ncpm_br',
    'new_cases_y':'nc_us',
    'new_cases_per_million_y':'ncpm_us'
}

df_covid_merge.rename(columns=dict_rename, inplace=True)

df_covid_merge
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
df_covid_merge.to_csv('df_resultado_aula_pandas.csv', sep=',', encoding='utf8', index=False)

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
df_covid_duplicada = pd.DataFrame()

for i in range(0,10):
    df_covid_duplicada = pd.concat([df_covid_duplicada, df_covid]).reset_index(drop=True)

df_covid_duplicada.info(memory_usage='deep')
#
#
#
#
#
#
df_covid_duplicada.drop_duplicates(inplace=True)

df_covid_duplicada.info(memory_usage='deep')
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
columns_to_cat = ['iso_code','continent','location']

for c in columns_to_cat:
    df_covid_duplicada[c] = df_covid_duplicada[c].astype('category')
#
#
#
#
#
#
df_covid_duplicada.info(memory_usage='deep')
#
#
#
#
#
#
#
#
columns_to_int = ['total_cases','new_cases','total_deaths','new_deaths']

for c in columns_to_int:
    df_covid_duplicada[c] = df_covid_duplicada[c].fillna(-1)
    df_covid_duplicada[c] = df_covid_duplicada[c].astype('int32')
#
#
#
#
#
#
df_covid_duplicada.info(memory_usage='deep')
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
